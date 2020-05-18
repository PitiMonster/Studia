#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <stdbool.h>


// tworzenie struktury zawierającej dane do wykonania operacji
typedef struct {
	int size;
	bool** matrix1;
	bool** matrix2;
	bool** resultMatrix;
} matrixMult;

// wypełnianie macierzy losowo 0 i 1 jeśli nie jest to resultMatrix
bool** alloc_matrix(int size, int fill) {
	srand(time(NULL) + getpid());
	
	bool** matrix = calloc(size, sizeof(bool*));
	
	for (int i = 0; i < size; i++) {
		matrix[i] = calloc(size, sizeof(bool));
		if (fill > 0) {
			for (int j = 0; j < size; j++) matrix[i][j] = rand() % fill;
		}
	}
	
	return matrix;
}

// deklarowanie mutex'a do kolejkowania wątków
pthread_mutex_t mutex;
int curr_row = 0;

void* mult(void* vargp) {
	matrixMult* m = (matrixMult*) vargp;
	
	while (curr_row < m->size) {

        // blokowanie dostępu do operacji, czekanie aż wątek skończy, żeby np. dwa nie robiły tego samego wiersza macierzy
		pthread_mutex_lock(&mutex);
		int row = curr_row;
		curr_row++;
		pthread_mutex_unlock(&mutex);
		
		for (int i = 0; i < m->size; i++) {
			for (int j = 0; j < m->size; j++) {
				m->resultMatrix[row][i] = (m->matrix1[row][j] & m->matrix2[j][i]);
				if (m->resultMatrix[row][i] == 1) break;
			}
		}
	}
	
	pthread_exit(0);
}

int main(int argc, char* argv[]) {
	if (argc < 3) {
		printf("Provide agruments:\n1. Matrix size;\n2. Thread number;\n");
		return 1;
	}
	
	int size = atoi(argv[1]);
	int tNumber = atoi(argv[2]);
	
	matrixMult matMult;
	
	matMult.size = size;
	matMult.matrix1 = alloc_matrix(size, 2);
	matMult.matrix2 = alloc_matrix(size, 2);
	matMult.resultMatrix = alloc_matrix(size, 0);
	
    // inicjalizowanie mutex'a
	pthread_mutex_init(&mutex, NULL);
	pthread_t threadIds[tNumber];
	
    // uruchamianie wszystkich wątków
	for (int i = 0; i < tNumber; i++) {
		printf("thread %d starting\n", i);
		pthread_create(&threadIds[i], NULL, &mult, &matMult);
	}
	
    // czekanie aż wszystie wątki zakończą pracę
	for (int i = 0; i < tNumber; i++) {
		pthread_join(threadIds[i], NULL);
		printf("thread %d finished\n", i);
	}
	
    // dealokowanie pamięci mutex'a
	pthread_mutex_destroy(&mutex);
	
	printf("done, exiting\n");
	return 0;
}
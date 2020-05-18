#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <fstream>
#include <sstream>
#include "../lista3/radix_sort.h"
#include <sys/sysinfo.h>

using namespace std;

int cmp = 1;
float bytes_num = 0;
// int comp_amount = 0;
// int moves_amount = 0;

// funckja wypisująca wejściową tablicę o podanej długości
void display(int *array, int n){

	for(int i = 0; i < n; i++){
		cout<<array[i]<<" ";
	}
	cout<<endl;
}

// funckja sprawdzająca poprawność posortowania wejściowej tablicy
bool validate(int *tab, int n){

	for(int i = 0; i < n-1; i++){
		if(tab[i]*cmp > tab[i+1]*cmp){
			return false;
		}
	}	
	return true;
}

// sortowanie tablicy wejściowej za pomocą algorytmu insertion sort
void insertion_sort(int *tab, int n) {
	int key;
	int j;
	for (int i = 1; i < n; i++) {
		key = tab[i];	// aktualny element do ustawienia na dobrym miejscu
		j = i - 1;
		// dopóki element za key jest od niego większy to go przesuwamy do tyłu
		while (key*cmp < tab[j]*cmp && j >= 0) {
			comp_amount++;
			moves_amount++;
			tab[j + 1] = tab[j];
			j--;
		}
		moves_amount++;

		// dodanie wyjściowego porównania z while które sprawiło, że opóściliśmy pętlę
		if( j >= 0){
			comp_amount++;
		}
		tab[j + 1] = key;	// ustawienie key na jego właściwe miejsce
	}

}

// funckja scalająca dwie posortowane części tablicy w jedną posortowaną
void merge(int *array, int left, int mid, int right){

	int i = left;
	int j = mid + 1;
	int temp_array[right-left+1];	// pomocnicza tablica
	int k = 0;
	// dopóki z lewej i z prawej strony są elementy nie scalone
	while(i <= mid && j <= right){
		
		// jeśli element z lewej tablicy jest mniejszy to wrzucenie go na tablicę pomocniczą
		if(array[i]*cmp < array[j]*cmp){
			temp_array[k] = array[i];
			i++;
			k++;
		}
		// jeśli element z prawej tablicy jest mniejszy to wrzucenie go na tablicę pomocniczą
		else{
			temp_array[k] = array[j];
			j++;
			k++;
			moves_amount++;
		}

		comp_amount++;
		
	}
	// wrzucenie na tablicę pomocniczą elementów z tablicy lewej które tam się jeszcze nie znajdują
	while(i <= mid){
		temp_array[k] = array[i];
		i++;
		k++;
	}
	// wrzucenie na tablicę pomocniczą elementów z tablicy prawej które tam się jeszcze nie znajdują
	while(j <= right){
		temp_array[k] = array[j];
		j++;
		k++;
	}

	// nadpisanie nieposortowanych elementów tablicy głównej przez posortowane już elementy tablicy pomocniczej
	for(int m = 0; m < k; m++){
		array[m+left] = temp_array[m];
	}
}

// funckja sortująca wejściową tablicę za pomocą algorytmu merge sort
void merge_sort(int *array, int left, int right){

	// jeśli został więcej niż jeden element do posortowania
	if(left < right){
		int mid = (left+right)/2;
		merge_sort(array, left, mid);	// sortowanie lewej części wejściowej tablicy
		merge_sort(array, mid+1, right); // sortowanie prawej części wejściowej tablicy
		merge(array, left, mid, right);	// scalanie wcześniej posortowanych obu części tablicy
	}
	
}

// funkcja sortująca tablicę na wejściu za pomocą algorytmu quick sort
void quick_sort(int *array, int left, int right){

	int i = left;
	int j = right;
	int mid = (right+left)/2;
	int pivot = array[mid];
	int temp;

	while(true){

		// szukanie wartości >= pivot na lewo od niego
		while(array[i]*cmp < pivot*cmp){
			i++;
			comp_amount++;
		}
		comp_amount++;

		// szukanie wartości <= pivot na prawo od niego
		while(array[j]*cmp > pivot*cmp){
			j--;
			comp_amount++;
		}
		comp_amount++;

		if(i <= j){
			// zamiana wartości tablicy
			temp = array[i];
			array[i] = array[j];
			array[j] = temp;
			j--;
			i++;
			moves_amount++;
		}
		else{
			break;
		}
	}

	if(j > left){	// jeśli z lewej został >1 element to sortujemy
		quick_sort(array, left, j);
	}
	if(i < right){	// jeśli z prawej został >1 element to sortujemy
		quick_sort(array, i, right);
	}
}

void swap(int *tab, int a, int b){
	int temp = tab[a];
	tab[a] = tab[b];
	tab[b] = temp;
}

void dual_quick_sort(int *array, int left, int right){

	if(left >= right){
		return;
	}

	int right_pivot, left_pivot;
	int i = left + 1;	// wskazuje na pierwszy element w tablicy nie mniejszy od left_pivot
	int j = i;			// wskazuje na pierwszy element od lewej, o którym nie wiemy gdzie powinien być
	int k = right - 1;	// wskazuje na ostatni element w tablicy nie większy od right_pivot 
	int diff_number = 0;

	// wzięcie pierwszego i ostatniego elementu tablicy jako pivoty; zamienienie ich jeśli są w złym porządku
	if(array[left]*cmp > array[right]*cmp){
		swap(array, left, right);
		moves_amount++;
	}
	comp_amount++;

	left_pivot = array[left];
	right_pivot = array[right];

	while(j <= k){
		if(diff_number*cmp >= 0){	// jeśli liczb < left_pivot jest więcej niż > right_pivot
			comp_amount++;
			if(array[j]*cmp < left_pivot*cmp){
				swap(array, i, j);	// rzucenie < left_pivot elementu za i
				diff_number ++;		// zwiększenie się liczby elementów < left_pivot
				j++;	// przejście na kolejny element do sprawdzenia
				i++;	// przejście na kolejny nie mniejszy niż left_pivot element 
				moves_amount++;
			}
			else{
				comp_amount++;
				if(array[j]*cmp < right_pivot*cmp){		// jeśli element ma być pomiędzy pivotami to tam zostaje
					j++;
				}
				else{
					// jeśli element jest > right_pivot to zamienienie go z k-tym elementem 
					// bo tam zbieramy wszystkie > right_pivot
					swap(array, j, k); 		
					diff_number--;	// zmniejszenie liczby elementów < left_pivot
					k--;
					moves_amount++;
				}
			}
		}
		else{	// jeśli liczb > right_pivot jest więcej niż < left_pivot
			comp_amount++;
			if(array[k]*cmp > right_pivot*cmp){
				diff_number--;	
				k--;
			}
			else{
				comp_amount++;
				if(array[k]*cmp < left_pivot*cmp){
					int temp = array[k];
					array[k] = array[j];	// k już nie wskazuje na tamten mniejszy element tylko na kolejny elment o którym nie mamy informacji
					array[j] = array[i];	// j teraz wskazuje na element który wskazywało i 	
					array[i] = temp;		// i terazz wskazuje na ostatni el<left_pivot, o którym wiemy

					i++;	// chcemy, aby i wskazywało na pierwszy element nie mniejszy od left_pivot
					diff_number++;

					moves_amount += 3;
				}
				else{
					swap(array, j, k);	// wiemy że ten element pozostanie pomiędzy pivotami więc rzucamy go na j i zostawiamy tam a k-ty element jeszcze sprawdzimy ponownie
					moves_amount++;
				}
				j++;	// przesuwamy się dalej by w sprawdzać kolejne elementy, o których nie wiemy gdzie mają być
			}
		}
	}

	swap(array, left, i-1);	// left_pivot teraz będzie oddzielał elementy mniejsze od siebie od tych większych
	swap(array, right, k+1);	//	right_pivot teraz będzie oddzielał elementy większe od siebie od tych mniejszych
	moves_amount += 2;
	dual_quick_sort(array, left, i-2); // powtarzamy operację na lewej części tablicy; i-1 element jest już na dobrym miejscu
	dual_quick_sort(array, i, k); // powtarzamy operację na środkowej części tablicy; k+1 element jest już na dobrym miejscu
	dual_quick_sort(array, k+2, right);		// powtarzamy operację na prawej części tablicy

}

// funkcja wywołująca sortowanie wybrane przez użytkownika
float choose_sort(char** argv, int *tab, int n){

	clock_t start;
	float time;

	if(string(argv[4]) == ">="){
		cmp = -1;
	}
	
	string sort = string(argv[2]);
	if(sort == "insert"){
		start = clock();
		insertion_sort(tab, n);
	}
	else if(sort == "merge"){
		start = clock();
		merge_sort(tab, 0, n-1);
	}
	else if(sort == "quick"){
		start = clock();
		quick_sort(tab, 0, n-1);
	}
	else if(sort == "dual_quick"){
		start = clock();
		dual_quick_sort(tab, 0, n-1);
	}
	else if(sort == "radix_sort"){
		cmp = 1;
		start = clock();
		radix_sort(tab,n);
	}
	else{
		cout<<"Podaj rodzaj< sortowania:\n1. insert\n2. merge\n3. quick\n4.dual_quick\n";
		return 0;
	}
	struct sysinfo si;
 	sysinfo (&si);
	bytes_num = si.freeram;
	time = float(clock() - start)/ CLOCKS_PER_SEC;
	
	return time;
}

int main(int argc, char** argv){
		
	int n;
	float exe_time;
	const double megabyte = 1024 ;

	struct sysinfo si;
	sysinfo (&si);
	float free_before = si.freeram;

	
	if(argc == 5){
		cout<<"Podaj liczbe elementow do posortowania: ";
		cin>>n;
		cout<<endl;

		int *tab;
		tab = new int [n];				// tworzenie tablicy o wielkości n
		cout<<"Podaj elementy do posortowania:\n";
		for(int i = 0; i < n; i++){
			cin>>tab[i];				// wypełnianie tablicy elementami od użytkownika
		}

		exe_time = choose_sort(argv, tab, n);	// użycie sortowania wybranego przez usera

		// sprawdzenie czy tablica została posortowana poprawnie
		if(!validate(tab, n)){
			cout<<"Tablica jest nie posortowana!\n";
			return 0;	
		}

		cout<<fixed;	// przejście na wypisywanie liczb ustalonych
		// wypisywanie wyników na ekran
		cout<<"Liczba porownan miedzy kluczami: "<<comp_amount<<endl;
		cout<<"Liczba przestawien kluczy: "<<moves_amount<<endl;
		cout<<"Czas dzialania funkcji sortujacej: "<<exe_time<<endl;
		cout<<"Liczba posortowanych elementow: "<<n<<endl;
		cout<<"Posortowana tablica elementow:\n";
		 printf ("free RAM   : %5.1f MB\n", free_before-bytes_num);
		display(tab, n);

		delete[] tab;
	}
	
	if(argc == 8){

		srand (time(NULL));
		int k;
		istringstream(string(argv[7])) >> k;

		ofstream my_file; // tworzenie i otwarcie pliku
		my_file.open((string(argv[6])), std::ofstream::app);
		int ranges[5] = {50, 500, 5000, 15000, 50000};
		for(int i = 50; i <100001; i *= 10){
			for(int s = 0; s < 5; s++){
				int limit = ranges[s];
				// wykonanie k powtórzeń
				for(int j = 0; j < k; j++){
					
					int *tab;
					tab = new int [i];	// tworzenie nowej tablicy o wielkości i

					for(int m = 0; m < i; m++){		// uzupełnianie tablicy losowymi wartościami
						tab[m] = rand() % limit;
					}

					exe_time = choose_sort(argv, tab, i);	// posortowanie elementów

						// wpisanie danych do pliku
					my_file<<i<<" "<<limit<<" "<<std::fixed<<exe_time<<" "<<argv[2]<<endl;

					comp_amount = 0;
					moves_amount = 0;

					delete[] tab;
						
				}
			}
		}

		my_file.close();
	}

	return 0;
}


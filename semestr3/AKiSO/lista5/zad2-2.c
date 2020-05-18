#include <stdio.h>
#include <signal.h>

int main() {
	printf("Wywolywanie wszystkich sygnalow na inicie \n");
	sleep(1);
	for (int i = 65; i > 0; i--) {
		printf("\nOdpalanie sygnalu nr.: %d\n", i);
		// sleep(1);
		printf("Rezultat: %d\n", kill(1, i));
	}
	printf("Przeszlo\n");
	return 0;
}

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int comp_amount = 0;
int moves_amount = 0;
int cmp = 1;

// wypisanie tablicy o podanych indeksach ograniczających
void display(int* tab,int left,int right){
    cout<<"Dane: ";
    for(int i = left; i <= right; i++){
        cout<<tab[i]<<" ";
    }
    cout<<endl;
}

// wyznaczenie mediany za pomocą insertion sort'a
int insertion_sort_median(int* tab, int left, int right){
    if(right - left == 0){
        return tab[left];
    }
    for(int i = left+1; i <= right; i++){
        int j = i-1;
        int temp = tab[i];
        while(temp < tab[j] && j >= left){
            comp_amount++;
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = temp;
        moves_amount++;
    }
    int mid = left + (right-left)/2;
    return tab[mid];    // zwracam mediane tej części listy
}

// wybranie pivota jako mediany median
// dzielenie wejściowej tablicy na 5-elementowe podzbiory
// wyznaczanie z nich median i na nich wykonywanie tego samego rekurencyjnie
// zwrócenie 'mediany median' jako pivot 
int choose_pivot(int* tab, int left,int right){
    // jeśli tablica nie ma wiecej niz 5 elemntów to nie ma sensu robić jej partycjonowania
    // i zwracam jej mediane
    if(right - left < 5){
        int mid = left + (right-left)/2;
        return insertion_sort_median(tab, left, right);
    }
    int* temp_arr;
    int n = ceil((right-left+1)/5); // ilość zbiorów 5 elementowych
    temp_arr = new int [n];
    int i = left;
    
    // wyznaczanie median wszystkich pozdzbiorów 5 elementowych
    for(int i = 0; i < n-1; i++){
        temp_arr[i] = insertion_sort_median(tab, left+i*5, left+4+i*5);
    }
    // dla ostatniego zbioru osobno bo nie wiemy czy nie jest on mniejszy
    // i nie chcemy wyjsc po za zakres tej czesci tablicy
    temp_arr[n-1] = insertion_sort_median(tab, left+5*(n-1), right); 

    // rekurencyjnie wykonujemy to samo na tablicy median
    int p = choose_pivot(temp_arr, 0, n-1);

    delete[] temp_arr;

    // zwracamy mediane median
    return p;
}

int select(int* tab, int left, int right, int index){
    // wyppisanie części tablicy, w której szukamy naszej liczby
    // display(tab, left, right);
    // cout<<"k = "<<index - left + 1<<endl;
    int temp;
    // jeśli tablica jest jednoelementowa to zwracamy ten element
    if(right - left == 0){
        return tab[left];
    }
    // jeżeli index = left to zwracam minimum z tej części tablicy
    if(index == left){
        int min = tab[left];
        int min_i = left;
        for(int i = left+1; i <= right; i++){
            comp_amount++;
            if(tab[i] < min){
                min = tab[i];
                min_i = i;
            }
        }
        // swap, aby najmniejsza liczba była na najniższym indeksie w tej części tablicy
        temp = tab[min_i];
        tab[min_i] = tab[left];
        tab[left] = temp;
        return min;
    }
    // jeżeli index = right to zwracam maximum z tej części tablicy
    if(index == right){
        int max = tab[left];
        int max_i = left;
        for(int i = left+1; i <= right; i++){
            comp_amount++;
            if(tab[i] > max){
                max = tab[i];
                max_i = i;
            }
        }
        // swap, aby nasza szukana liczba była na dobrym indeksie
        temp = tab[right];
        tab[right] = tab[max_i];
        tab[max_i] = temp;
        return max;
    }
    
    int i = left;
    int j = right;
    int pivot = choose_pivot(tab, left, right); // pivot jako 'mediana median'
    int answer;

    // cout<<"Pivot = "<<pivot<<endl;
    // tu jest wykonywany zwykłe partycjonowanie
    while(true){

        comp_amount++;
        while(tab[i] < pivot){
            i++;
            comp_amount++;
        }

        comp_amount++;
        while(tab[j] > pivot){
            j--;
            comp_amount++;
        }

        if(j>i){
            // cout<<"Swap "<<tab[i]<<" z "<<tab[j]<<" \n";
            temp = tab[j];
            tab[j] = tab[i];
            tab[i] = temp;
            moves_amount++;

            if(tab[i] == pivot && tab[j] == pivot && i != j){
                j--;
                i++;
                comp_amount++;
            }
            comp_amount++;
        }
        else{
            break;
        }
    }

    if(j == index){
        return tab[j];
    }
    // jeśli index jest po lewej od pivota 
    if(j > index){
        answer = select(tab, left, j-1, index);
    }
    else{
        // jeśli index jest po prawej od pivota
        answer = select(tab, j+1, right, index);
    }
    // wartość liczby szukanej
    return answer;
}

// funkcja sortująca tablicę na wejściu za pomocą algorytmu quick sort
void quick_sort(int *array, int left, int right){

	int i = left;
	int j = right;
	int mid = (right+left)/2;
	int pivot = select(array, left, right, mid);
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
    int one_third = left + (right-left)/3;
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
    int temp_left_pivot = select(array, left, right,one_third);
    int left_index = 0;
    for(int i = left; i <= right; i++){
        if(array[i] == temp_left_pivot){
            left_index = i;
            break;
        }
    }
    swap(array, left_index, left);
    int temp_right_pivot = select(array, left, right, 2*one_third);
    int right_index = 0;
    for(int i = right; i >= left; i--){
        if(array[i] == temp_right_pivot){
            right_index = i;
            break;
        }
    }
    swap(array, right_index, right);

	left_pivot = array[left];
	right_pivot = array[right];
	if(left_pivot*cmp > right_pivot*cmp){
		swap(array, left, right);
		left_pivot = array[left];
		right_pivot = array[right];
	}

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
	if(sort == "quick"){
		start = clock();
		quick_sort(tab, 0, n-1);
	}
	else if(sort == "dual_quick"){
		start = clock();
		dual_quick_sort(tab, 0, n-1);
	}
	else{
		cout<<"Podaj rodzaj< sortowania:\n1. insert\n2. merge\n3. quick\n4.dual_quick\n";
		return 0;
	}

	time = float(clock() - start)/ CLOCKS_PER_SEC;
	
	return time;
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

int main(int argc, char** argv){
		
	int n;
	float exe_time;
	
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
		display(tab,0, n-1);

		delete[] tab;
	}
	
	if(argc == 8){

		srand (time(NULL));
		int k;
		istringstream(string(argv[7])) >> k;

		ofstream my_file; // tworzenie i otwarcie pliku
		my_file.open((string(argv[6])), std::ofstream::app);

		for(int i = 100; i <10001; i += 100){
			// wykonanie k powtórzeń
			for(int j = 0; j < k; j++){
				int *tab;
				tab = new int [i];	// tworzenie nowej tablicy o wielkości i

				for(int m = 0; m < i; m++){		// uzupełnianie tablicy losowymi wartościami
					tab[m] = rand() % (100000+i);
				}

				exe_time = choose_sort(argv, tab, i);	// posortowanie elementów

				my_file<<i<<" "<<comp_amount<<" "<<moves_amount<<" "<<fixed<<exe_time<<" "<<argv[2]<<endl;	// wpisanie danych do pliku

				comp_amount = 0;
				moves_amount = 0;

				delete[] tab;
			}
		}

		my_file.close();
	}

	return 0;
}
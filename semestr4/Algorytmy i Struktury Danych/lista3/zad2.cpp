#include <iostream>
#include <stdlib.h>  
#include <cmath>
#include <string>
#include <random>
#include <bits/stdc++.h> 
#include <algorithm>

using namespace std;

int comp_number = 0;
int moves_number = 0;

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
            comp_number++;
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = temp;
        moves_number++;
    }
    int mid = left + (right-left)/2;
    return tab[mid];    // zwracam mediane tej części listy
}

int randomized_selection(int* tab, int left, int right, int index){
    display(tab, left, right);
    cout<<"k = "<<index - left + 1<<endl;
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
            comp_number++;
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
            comp_number++;
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
    int mid = i + (j-i)/2;
    int pivot = tab[mid];
    int answer;

    cout<<"Pivot = "<<pivot<<endl;

    // tu jest wykonywane zwykłe partycjonowanie
    while(true){

        comp_number++;
        while(tab[i] < pivot){
            i++;
            comp_number++;
        }
        
        comp_number++;
        while(tab[j] > pivot){
            j--;
            comp_number++;
        }

        if(j>i){
            cout<<"Swap "<<tab[i]<<" z "<<tab[j]<<" \n";
            temp = tab[j];
            tab[j] = tab[i];
            tab[i] = temp;
            moves_number++;
            if(tab[i]== pivot && tab[j] == pivot && i != j){
                j--;
                i++;
                comp_number++;
            }
            comp_number++;
        }
        else{
            break;
        }
    }

    if(j == index){
        return tab[j];
    }
    if(j > index){
        answer = randomized_selection(tab, left, j-1, index);
    }
    else{
        answer = randomized_selection(tab, j+1, right, index);
    }
    return answer;
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
    display(tab, left, right);
    cout<<"k = "<<index - left + 1<<endl;
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
            comp_number++;
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
            comp_number++;
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

    cout<<"Pivot = "<<pivot<<endl;
    // tu jest wykonywany zwykłe partycjonowanie
    while(true){

        comp_number++;
        while(tab[i] < pivot){
            i++;
            comp_number++;
        }

        comp_number++;
        while(tab[j] > pivot){
            j--;
            comp_number++;
        }

        if(j>i){
            cout<<"Swap "<<tab[i]<<" z "<<tab[j]<<" \n";
            temp = tab[j];
            tab[j] = tab[i];
            tab[i] = temp;
            moves_number++;

            if(tab[i] == pivot && tab[j] == pivot && i != j){
                j--;
                i++;
                comp_number++;
            }
            comp_number++;
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

// liczenie średniej wartości tablicy wejściowej
float average(int* tab, int n){
    int avg = 0;
    for(int i = 0; i < n; i++){
        avg += tab[i];
    }

    return avg/n;
}

float standard_deviation(int* tab, int n){
    int avg = average(tab, n);

    int dev = 0;
    int temp;

    for(int i = 0; i < n; i++){
        temp = tab[i] - avg;
        dev += temp*temp;
    }

    return sqrt(dev/n);
}

int main(int argc, char** argv){
    
    if(argc == 2){

        srand(time(NULL));

        int* random_select_tab;
        int* select_tab;
        int n;
        int temp;
        int array_random_select_comp_num[20];
        int array_random_select_moves_num[20];
        int array_select_comp_num[20];
        int array_select_moves_num[20];

        cout<<"Podaj liczbe elementow tablicy"<<endl;
        cin>>n;
        random_select_tab = new int[n];
        select_tab = new int[n];
        string operation = string(argv[1]);
        if(operation == "-r"){

            for(int i = 0; i < n; i++){
                temp = rand() % 5000 + 1;
                random_select_tab[i] = temp;
                select_tab[i] = temp;
            }
        }
        else if(operation == "-p"){
            bool* temp_arr;
            temp_arr = new bool[n+1];
            for(int i = 0; i < n+1; i++){
                temp_arr[i] = false;
            }

            int k = rand() % n + 1;
            for( int i = 0; i < n; i++){
                while(temp_arr[k] != false){
                    k = rand() % n + 1;
                }
                random_select_tab[i] = k;
                select_tab[i] = k;
                temp_arr[k] = true;
            }
        }
        else{
            cout<<"Błędne paramtery wejściowe"<<endl;
            return 0;
        }

        // cout<<"Podaj elementy"<<endl;
        
        // for(int i = 0; i <n; i++){
        //     cin>>tab[i];
        // }
        int index;
        cout<<"Podaj index szukanej z kolei wartości"<<endl;
        cin>>index;
        for(int m = 0; m < 20; m++){

            cout<<"Teraz będą wyświetlone dane dla algorytmu random select"<<endl;
            int value_random_select = randomized_selection(random_select_tab, 0, n-1, index-1);

            int random_comp_num = comp_number;
            int random_moves_num = moves_number;

            comp_number = 0;
            moves_number = 0;

            cout<<"\n\nTeraz będą wyświetlone dane dla algorytmu select"<<endl;
            int value_select = select(select_tab, 0, n-1, index-1);
            
            cout<<"\nTeraz tablica wynikowa, liczba porównań i przestawień algorytmu random select"<<endl;
            for(int i = 0; i < n; i++){
                if(i == index-1){
                    cout<<"["<<random_select_tab[i]<<"] ";
                }
                else{
                    cout<<random_select_tab[i]<<" ";
                }
            }
            cout<<"Liczba porównań: "<<random_comp_num;
            cout<<"\nLiczba przestawień: "<<random_moves_num<<endl;

            cout<<"\nTeraz tablica wynikowa, liczba porównań i przestawień algorytmu select"<<endl;
            for(int i = 0; i < n; i++){
                if(i == index-1){
                    cout<<"["<<select_tab[i]<<"] ";
                }
                else{
                    cout<<select_tab[i]<<" ";
                }
            }

            cout<<"\nLiczba porównań: "<<comp_number;
            cout<<"\nLiczba przestawień: "<<moves_number<<endl;

            array_random_select_comp_num[m] = random_comp_num;
            array_random_select_moves_num[m] = random_moves_num;
            array_select_comp_num[m] = comp_number;
            array_select_moves_num[m] = moves_number;
        }

        cout<<"Średnie:\n";
        cout<<average(array_random_select_comp_num,20)<<" "<<average(array_random_select_moves_num, 20)<<endl;
        cout<<average(array_select_comp_num,20)<<" "<<average(array_select_moves_num, 20)<<endl;

        cout<<"Odchylenia:\n";
        cout<<standard_deviation(array_random_select_comp_num,20)<<" "<<standard_deviation(array_random_select_moves_num, 20)<<endl;
        cout<<standard_deviation(array_select_comp_num,20)<<" "<<standard_deviation(array_select_moves_num, 20)<<endl;
        
        
        delete[] random_select_tab;
        delete[] select_tab;

    }

    return 0;
}
#include <iostream>
#include <stdlib.h>

using namespace std;

int comp_amount = 0;
int moves_amount = 0;

void sort_by_num(int* tab, int* temp_arr, int pow, int n){
    int rests[10] = {0};
    for(int i = 0; i < n; i++){
        rests[(tab[i]/pow) % 10]++;
    }
    for(int i = 1; i<10;i++){
        rests[i] += rests[i-1];
    }
    for(int i = n-1; i >=0; i--){
        moves_amount++;
        int position = (tab[i]/pow) % 10;
        temp_arr[rests[position]-1] = tab[i];
        rests[position]--;
    }
    for(int i = 0; i < n; i++){
        moves_amount++;
        tab[i] = temp_arr[i];
    }
}

void radix_sort(int* tab, int n){

    int max = tab[0];
    for(int i = 1; i < n; i++){
        comp_amount++;
        if(tab[i] > max){
            max = tab[i];
        }
    }
    int* temp_arr = new int[n];

    for(int pow = 1; max/pow > 0; pow*=10){
        sort_by_num(tab, temp_arr, pow, n);
    }
    delete[] temp_arr;
}

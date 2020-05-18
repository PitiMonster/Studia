#include <iostream>
#include <stdio.h>
#include "radix_sort.h"
#include <random>

using namespace std;

int rec_num = 0;
bool binary_search(int* tab, int value, int left, int right){
    if(right < left){
        return false;
    }
    int mid = left + (right-left)/2;
    comp_amount++;
    if(value == tab[mid]){
        return true;
    }
    comp_amount++;
    rec_num++;
    // cout<<rec_num<<" "<<left<<" "<<right<<endl;
    if(value < tab[mid]){
        return binary_search(tab, value, left, mid-1);
    }
    else{
        return binary_search(tab, value, mid+1, right);
    }
}


int main(){

    int* arr;
    int n;
    srand(time(NULL));

    cout<<"Podaj ilośc elementów tablicy"<<endl;
    cin>>n;

    arr = new int [n];
    cout<<"Podaj posortowane elementy tablicy\n";
    for(int i = 0; i < n; i++){
        cin>>arr[i];
        // arr[i] = rand() % 2000 + 1;
    }
    // radix_sort(arr, n);
    cout<<"\nPodaj liczbe do wyszukania: ";
    int v;
    cin>>v;

    comp_amount = 0;
    moves_amount = 0;
    cout<<"Wynik wyszukiwania: "<<binary_search(arr, v, 0, n-1)<<endl;
    // rec_num = 0;
    // comp_amount = 0;
    // cout<<binary_search(arr, 5000, 0, n-1)<<endl;
    printf("Liczba wywolan rekurencyjnych: %d\n",rec_num);
    cout<<"Liczba porownan elementow tablicy: "<<comp_amount<<endl;

    return 0;
}
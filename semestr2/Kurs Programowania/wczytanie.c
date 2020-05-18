//wczytanie.c
#include "funs.h"
#include <stdio.h>

void wczytanie()
{
    char wyraz[100];
    printf("Podaj wyraz do sprawdzenia: ");
    scanf("%s", &wyraz);
    if(palindrom(wyraz)){
        printf("\"%s\" jest palindromem\n",wyraz);
    } else {
        printf("\"%s\" nie jest palindromem\n",wyraz);
    }
}

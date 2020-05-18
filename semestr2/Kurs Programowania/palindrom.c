//palindrom.c
#include "funs.h"
#include <stdbool.h>
#include <string.h>

bool palindrom(char wyraz[]){

    int dlugosc = strlen(wyraz);
    int a = 0, b = dlugosc-1;
    while(a<=b){
        if(wyraz[a]!=wyraz[b]){
            return 0;
        }
        a++;
        b--;
    }
    return 1;
}


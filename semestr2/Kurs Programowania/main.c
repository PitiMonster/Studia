#include <stdio.h>
#include <math.h>
#include "funs.h"

int main(int argc, char **argv)
{
    long double a,b,e;
    FILE *fp;
    if(argc < 2){
        printf("Musisz podac jakis plik\n");
        return 0;
    } else {
        fp = fopen(argv[1],"r");
        if(fp==NULL){
            printf("Plik nie istnieje\n");
            return 0;
        }
        fscanf(fp,"%Lf",&a);
        fscanf(fp,"%Lf",&b);
        fscanf(fp,"%Lf",&e);
    }
    printf("%.8Lf\n",rozwiazanie(a,b,e));
    return 0;
}

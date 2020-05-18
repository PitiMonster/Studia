#include <stdio.h>

int main(void){
	for(int i=1; i<=256; i++){
		printf("\033[38;5;%dmHello World!\n", i);
	}
	return 0;
}

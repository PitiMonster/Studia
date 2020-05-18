#include "funs.h"
#include <stdio.h>

long double rozwiazanie(long double a, long double b, long double eps){
	while(b - a > eps){
		long double sr = (a+b)/2;
		if(f(sr)*f(a)<0){
			b = sr;
		}
		else{
			a = sr;
		}
	}
	return b;

	/*
	for(long double i=a; i<b; i=i+eps){
        if(f(i)*f(i+eps)<=0){
            return i;
        }
    }
    return 0;*/
}

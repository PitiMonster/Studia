package com.company;

public class Main {

    public static boolean czypierwsza(int a){
        for(int i = 2; i*i<=a; i++){
            if(a%i==0)return false;
        }
        return true;

    }
    public static int pierwsza(int n){
        int a = n+1;
        while(a%10!=9)a++;
        if(czypierwsza(a))return a;
        else return pierwsza(a+9);
    }
    public static void main(String[] args) {

	for(int i = 1; i<=1000; i++)
	    System.out.println(i+": "+pierwsza(i));
	System.out.println(pierwsza(250101));
    }
}

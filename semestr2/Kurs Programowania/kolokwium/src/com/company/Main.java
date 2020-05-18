package com.company;

public class Main {

    public static void main(String[] args) {

        int a = 0;
        int b = 1;
        int i = 1;
        int c;
        int n = Integer.parseInt(args[0]);

        while(true){
            i++;
            c = b;
            b = (a + b) % 10;
            if ( b-a < 0) a = a -b;
            else a = b - a;
            if(a < 0 ) a  = a *-1;
            System.out.println(b);
            if(b == 7 && i >= n) break;

        }
        System.out.println(i);

    }
}

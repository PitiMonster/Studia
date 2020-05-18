package com.company;

/*
    args[0] - ilosc pol planszy po X
    args[1] - ilosc pol planszy po Y
    args[2] - parametr szybkosci rozgrywki
    args[3] - ilosc krolikow na start
*/

public class Main {

    public static void main(String[] args) throws InterruptedException {

            // parametry planszy X na Y
            int x = Integer.parseInt(args[0]);
            int y = Integer.parseInt(args[1]);

            // szybkosc gry
            int k = Integer.parseInt(args[2]);

            // ilosc krolikow na start
            int rabbitsAmount = Integer.parseInt(args[3]);

            new MyFrame(x, y, k, rabbitsAmount);
            // write your code here

    }
}

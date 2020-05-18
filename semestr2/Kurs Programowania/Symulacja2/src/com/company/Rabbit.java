package com.company;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class Rabbit extends Thread{
    boolean isAlive;
    int x = 0;
    int y = 0;
    int prevX = 0;
    int prevY = 0;
    MyCanvas canvas;

    // temp point to create point with rabbit position
    private Point tempPoint;

    // tablica typu Point z mozliwymi ruchami krolika
    ArrayList<Point> possibleRabbitMoves;

    // aktualna odleglosc krolika od wilka
    private int currentDisatanceFromWolf;

    // nazwa krolika i watek w ktorym sie on wywola
    private String rabbitName;
    private Thread t;

    // konstruktor klasy Rabbit canvasa oraz ID tworzonego krolika
    public Rabbit(MyCanvas canvas, int rabbitID) {
        this.isAlive = true;
        this.canvas = canvas;
        this.rabbitName = "rabbit"+rabbitID;

        x = 0;
        y = 0;

        // poczatkowe ustawienie krolika na polu
        while(canvas.fieldsState[x][y] != 0) {
            x = (int) (Math.random() * (canvas.mapWidth));
            y = (int) (Math.random() * (canvas.mapHeight));
        }

        canvas.changePosition(x,y,prevX,prevY, true);

    }


    @Override
    public void run() {
        while(this.isAlive){

            prevX = x;
            prevY = y;

            // deklarowanie nowej tablicy na mozliwe ruchy zajaca
            possibleRabbitMoves = new ArrayList<>();

            // aktualny dystans krolika od wilka
            currentDisatanceFromWolf = (canvas.getWolfPosition().x - prevX)*(canvas.getWolfPosition().x - prevX) + (canvas.getWolfPosition().y - prevY)*(canvas.getWolfPosition().y - prevY);


            // sprawdzanie pol na okolo krolika i wybranie tych ktore go oddalaja od wilka
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    int newX = i - 1;
                    int newY = j - 1;
                    if((canvas.getWolfPosition().x - (prevX + newX))*(canvas.getWolfPosition().x - (prevX + newX)) + (canvas.getWolfPosition().y - (prevY + newY))*(canvas.getWolfPosition().y - (prevY + newY)) > currentDisatanceFromWolf){
                        if(canvas.isInBoard(prevX + newX, prevY + newY) && canvas.fieldsState[prevX + newX][prevY + newY] == 0){
                            tempPoint = new Point(prevX+newX,prevY + newY);
                            possibleRabbitMoves.add(tempPoint);
                        }
                    }
                }
            }


            // jesli moze sie ruszyc to wybiera ruch
            if(possibleRabbitMoves.size() > 0) {
                // losowanie pola na ktore ruszy sie krolik
                int i = RandomGenerator.nextInt(possibleRabbitMoves.size());

                tempPoint = possibleRabbitMoves.get(i);

                x = tempPoint.x;
                y = tempPoint.y;

                canvas.changePosition(x,y,prevX,prevY,true);
            }

            try {
                int sleepTime = RandomGenerator.nextInt(canvas.k) + canvas.k/2;
                Thread.sleep(sleepTime);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void start(){
        if(t == null){
            t = new Thread(this, rabbitName);
            t.start();
        }
    }

    // funkcja zabijajaca krolika
    public void kill(){
        this.isAlive = false;
        stop();
    }
}

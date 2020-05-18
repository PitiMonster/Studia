package com.company;

import java.awt.*;

public class Wolf extends Thread {

    private String wolfName = "Wolf";
    private Thread t;
    private int prevX = 0;
    private int prevY = 0;
    private int x;
    private int y;
    private MyCanvas canvas;
    private Point wolfPosition = new Point();


    // zmienna przexhowujaca ile czasu wilk musi czekac na ruch
    private int waitingTime;



    // konstruktor klasy Wolf biorący canvasa
    public Wolf(MyCanvas canvas){
        this.canvas = canvas;
        waitingTime = 0;

        // poczatkowe ulozenie wilka na planszy
        x = (int)(Math.random()*(canvas.mapWidth));
        y = (int)(Math.random()*(canvas.mapHeight));

        setWolfLocalization(x,y);

        canvas.changePosition(x,y,prevX,prevY,false);
    }

    @Override
    public void run() {
        while(true) {
            if (waitingTime == 0) {
                prevX = x;
                prevY = y;

                Point closestRabbit = canvas.getClosestRabbitPosition();
                int currentDistanceFromRabbit = (x - closestRabbit.x) * (x - closestRabbit.x) + (y - closestRabbit.y) * (y - closestRabbit.y);
                Point tempPoint = new Point(prevX, prevY);
                int closestDistanceFromRabbit = currentDistanceFromRabbit;

                // sprawdzenie po kolei wszystkich pol w okolicy wilka - z ktorego ma najblizej do najblizszego krolika
                for(int i = 0; i < 3; i++){
                    for( int j = 0; j < 3; j++){
                        int newX = i - 1;
                        int newY = j - 1;
                        if ((closestRabbit.x - (prevX + newX)) * (closestRabbit.x - (prevX + newX)) + (closestRabbit.y - (prevY + newY)) * (closestRabbit.y - (prevY + newY)) < closestDistanceFromRabbit) {
                            if(canvas.isInBoard(prevX + newX, prevY + newY)){
                                tempPoint = new Point(prevX+newX,prevY + newY);
                                closestDistanceFromRabbit = (closestRabbit.x - (prevX + newX)) * (closestRabbit.x - (prevX + newX)) + (closestRabbit.y - (prevY + newY)) * (closestRabbit.y - (prevY + newY));
                            }
                        }
                    }
                }


                // przypisanie nowej pozycji wilka do punktow x i y
                x = tempPoint.x;
                y = tempPoint.y;

                // sprawdzenie ktorego krolika zjadl wilk i usuniecie go
                if (closestDistanceFromRabbit == 0) {
                    for (int i = 0; i < canvas.startingRabbits.length; i++) {
                        if (canvas.startingRabbits[i].x == x && canvas.startingRabbits[i].y == y) {
                            canvas.startingRabbits[i].kill();
                            waitingTime = 5;
                            break;
                        }
                    }
                }


                // uaktualnienie zmiennej przechowujacej aktualne polozenie wilka
                setWolfLocalization(x, y);


                // zmienienie poycji wilka
                canvas.changePosition(x, y, prevX, prevY, false);

                // spanie watku
                try {
                    int sleepTime = RandomGenerator.nextInt(canvas.k) + canvas.k / 2;
                    Thread.sleep(sleepTime);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }


            } else {
                waitingTime -= 1;
            }
        }
    }

    // metoda startujaca watek
    public void start(){
        if(t == null){
            t = new Thread(this,wolfName);
            t.start();
        }
    }

    // metoda pobierajaca aktualna pozycje krolika
    public Point getWolfPosition(){
        return wolfPosition;
    }

    // metoda uaktualniajaca zmienna przechowujaca aktualna pozycje wilka
    private void setWolfLocalization(int x, int y){
        wolfPosition.x = x;
        wolfPosition.y = y;
    }
}

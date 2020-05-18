package com.company;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class MyCanvas extends JPanel {

    // dlugosc boku pola
    public int fieldSize = 20;
    private JFrame mainFrame;

    // szerokosc i dlugosc planszy
    int mapWidth;
    int mapHeight;
   // Point p = new Point(-fieldSize,0);
    // tablica int trzymajaca aktualny stan kazdego pola
    int[][] fieldsState;

    // tworzenie obiektu wilka
    Wolf w1;

    // zmienna przechowuja ilosc krolikow na starcie
    private int rabbitsAmount;

    // tablica typu Point z mozliwymi ruchami wilka
    ArrayList<Point> possibleWolfMoves;

    // wartosc odleglosc krolika od wilka
    private int deltaRabbit;

    // tablica typu Rabbit trymajaca utworzone na poczatku kroliki aby je odpalic dopiero po ulozeniu
    Rabbit[] startingRabbits;

    // sprawdzenie czy juz ulozono kroliki
    private boolean isPlacingFinished = false;

    // parametr k predkosci programu
    public int k;


    // konstruktor klasy MyCanvas otrzymujacy frame, ilosc pol po X i po Y
    public MyCanvas(JFrame frame, int x, int y, int k, int rabbitsAmount) {
        this.mainFrame = frame;
        this.mapWidth = x;
        this.mapHeight = y;
        this.k = k;
        this.rabbitsAmount = rabbitsAmount;
        startingRabbits = new Rabbit[this.rabbitsAmount];
        this.fieldsState = new int[x+1][y+1];
        w1 = new Wolf(this);
        for(int i = 0; i < this.rabbitsAmount; i++) startingRabbits[i] = new Rabbit(this, i);
        isPlacingFinished = true;
        for(int i = 0; i < this.rabbitsAmount; i++) startingRabbits[i].start();

        w1.start();



    }



    public void paintComponent(Graphics g){
        //tworzenie nowego punktu w lewym gornym rogu planszy aby ja rysowac
        Point p = new Point(-fieldSize,0);
        Graphics2D g2d =(Graphics2D) g;

        super.paintComponent(g);

        // rysowanie planszy
        for(int i = 0; i < mapWidth; i++){
            p.x = (int) p.getX() + fieldSize;
            p.y = 0;
            for(int j = 0; j < mapHeight; j++){
                //wybieranie koloru pola
                if(fieldsState[i][j] == 0) g.setColor(Color.white);
                else if(fieldsState[i][j] == 1) g.setColor(Color.blue);
                else g.setColor(Color.red);
                g.fillRect(p.x,p.y,fieldSize,fieldSize);
                g.setColor(Color.black);
                g.drawRect(p.x,p.y,fieldSize,fieldSize);

                g.drawRect(p.x,p.y,fieldSize,fieldSize);

                p.y = (int) (p.getY() + fieldSize);
            }

        }


    }

    public void changePosition(int x, int y, int prevX, int prevY, boolean isRabbit){
        if(isPlacingFinished == true) fieldsState[prevX][prevY] = 0;
        if(isRabbit == true) fieldsState[x][y] = 1;
        else fieldsState[x][y] = 2;

        this.repaint();
        this.revalidate();
    }

    // pobranie pozycji wilka
    public Point getWolfPosition(){
        return w1.getWolfPosition();
    }

    // zwrocenie array lista typu Point z krolikami najblizej wilka w danej chwili
    public Point getClosestRabbitPosition(){
        Point wolfPosition = getWolfPosition();
        Point tempPoint = new Point(-1,-1);
        deltaRabbit = mapHeight*mapWidth*mapWidth*mapHeight;

        // sprawdzenie pozycji wszystkich krolikow na mapie i wybranie tego najblizej wilka
        for(int i = 0; i < mapWidth; i++){
            for(int j = 0; j < mapHeight; j++){
                if(fieldsState[i][j] == 1){
                    if((wolfPosition.x - i)*(wolfPosition.x - i) + (wolfPosition.y - j)*(wolfPosition.y - j) < deltaRabbit){
                        deltaRabbit = (wolfPosition.x - i)*(wolfPosition.x - i) + (wolfPosition.y - j)*(wolfPosition.y - j);
                        tempPoint = new Point(i,j);
                    }
                }
            }

        }
        // jesli punkt nie ulegl zmianie( nie ma zadnego krolika na mapie) - koniec programu
        if(tempPoint.x == -1 && tempPoint.y == -1 ) System.exit(0);
        return tempPoint;
    }


    // sprawdzenie czy punkt jest na planszy
    public boolean isInBoard(int x, int y){
        if(x < 0 || x >= mapWidth || y < 0 || y >= mapHeight) return false;
        else return true;
    }


}

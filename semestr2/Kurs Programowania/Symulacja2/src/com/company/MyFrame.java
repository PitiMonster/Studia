package com.company;

import javax.swing.*;
import java.awt.*;

//Creating main frame

public class MyFrame extends JFrame {

    public MyFrame(int x, int y, int k, int rabbitsAmount) throws InterruptedException {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container pane = getContentPane();

        //tworzenie nowego canvas i danie mu ilosci pól na planszy
        MyCanvas canvas = new MyCanvas(this,x,y,k, rabbitsAmount);

        pane.add(canvas);

        this.pack();

        this.setSize(x*canvas.fieldSize + canvas.fieldSize/2,y*canvas.fieldSize + canvas.fieldSize/2*3);
        this.setResizable(false);

        this.setLocationRelativeTo(null);

        this.setVisible(true);
    }
}

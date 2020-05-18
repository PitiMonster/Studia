package com.company;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;

/**
 * Klasa zawierająca panel przycisków
 */
public class PanelWithFigures extends  JPanel {


    /**
     * Metoda uzupełniająca panel przycisków
     * @param canvas
     */
    public PanelWithFigures(MyCanvas canvas) {
        setLayout(new GridLayout(20,1));


        JButton kolo = new JButton("Koło");
        JButton prostokat = new JButton("Prostokąt");
        JButton wielokat = new JButton("Wielokąt");
        JButton kolor = new JButton("Ustaw kolor");
        JButton resize = new JButton("Zmień położenie");
        JButton save = new JButton("Zapisz obraz");
        JButton read = new JButton("Wczytaj obraz");


        kolo.addActionListener(e -> {
            canvas.setCurrentState(Figury.DRAW.toString());
            canvas.setFigureName(Figury.ELIPSA.toString());
            System.out.println(canvas.getFigureName());

            // canvas.shapeName = new Ellipse2D();
            canvas.shapeName = new Ellipse2D.Double();
        });

        prostokat.addActionListener(e -> {
            canvas.setCurrentState(Figury.DRAW.toString());
            canvas.setFigureName(Figury.PROSTOKAT.toString());
            System.out.println(canvas.getFigureName());

            canvas.shapeName = new Rectangle();
        });


        wielokat.addActionListener(e -> {
            System.out.println(canvas.getFigureName());
            canvas.setCurrentState(Figury.DRAW.toString());
            canvas.setFigureName(Figury.WIELOKAT.toString());
            canvas.shapeName = new Polygon();
        });

        kolor.addActionListener(e -> {
            Color newColor = JColorChooser.showDialog(this,"set color",canvas.currentColor);
            if(newColor != null) {
                canvas.currentColor = newColor;
                canvas.setCurrentState(Figury.KOLOR.toString());
            }

        } );

        resize.addActionListener(e -> {
            canvas.setCurrentState(Figury.RESIZE.toString());
        });

        save.addActionListener(e -> {
            canvas.setCurrentState(Figury.SAVE.toString());
        });

        read.addActionListener(e -> {
            canvas.setCurrentState((Figury.LOAD.toString()));
        });

        add(kolo);
        add(prostokat);
        add(wielokat);
        add(kolor);
        add(resize);
        add(save);
        add(read);

        setVisible(true);
    }

}

package com.company;

import javax.swing.*;
import java.awt.*;

public class CreateFrame {

    static JPanel panel;

    //TODO serializacja będziee wczytywała za każdym razem frame od początku będziemy zapiswać na szybko cały obraz i tworzyć nowy ze zmienionym obiektem edytowanym

    /**
     * Klasa tworząca głowny frame
     */
    // kontruuktor klasy
    public CreateFrame() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container pane = frame.getContentPane();

        MyCanvas canvas = new MyCanvas(frame);

        panel = new PanelWithFigures(canvas);
        pane.add(panel, BorderLayout.LINE_END);
        pane.add(canvas);


        frame.pack();

        // changin the size of frame to screen size
        Dimension screenSize= Toolkit.getDefaultToolkit().getScreenSize();
        frame.setSize(screenSize.width/2,screenSize.height/2);


        // center frame on the screen
        frame.setLocationRelativeTo(null);

        frame.setVisible(true);
    }
}
package com.company;

import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.geom.Area;
import java.awt.geom.PathIterator;
import java.util.ArrayList;

/**
 * Klasa NamedShape będąca tworzonym i edytowanym przez użytkownika obiektem
 */
public class NamedShape {
    private String name;
    private Shape shape;
    public Color color;
    //private ArrayList<Point> points;

    public NamedShape(String name, Shape shape, Color color) {
        this.name = name;
        this.shape = shape;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public Shape getShape() {
        return shape;
    }

    public void setShape(Shape shape) {this.shape = shape;}

    public Color getColor() {
        return color;
    }


//    public ArrayList<Point> getPoints() {
//        if (getName().equals("ELIPSA")) {
//            ArrayList<Point> points = new ArrayList<>();
//            points.add(new Point(getShape().getBounds().x, getShape().getBounds().y));
//            points.add(new Point(getShape().getBounds().width, getShape().getBounds().height));
//            System.out.println(points);
//            return points;
//        } else {
//            ArrayList<Point> points = new ArrayList<>();
//            float[] coords = new float[2];
//            PathIterator pathIterator = shape.getPathIterator(new AffineTransform());
//            while (!pathIterator.isDone()) {
//                switch (pathIterator.currentSegment(coords)) {
//                    case PathIterator.SEG_MOVETO:
//                        points.add(new Point((int) coords[0], (int) coords[1]));
//                        break;
//                    case PathIterator.SEG_LINETO:
//                        points.add(new Point((int) coords[0], (int) coords[1]));
//                        break;
//                    case PathIterator.SEG_CLOSE:
//                        break;
//                }
//                pathIterator.next();
//            }
//            return points;
//        }
//
//
//
//    }
}

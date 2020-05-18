package com.company;



import org.json.JSONException;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Klasa MyCanvas odpowiadająca za rysowanie i edycje figur
 */
public class MyCanvas extends JPanel implements MouseMotionListener, MouseListener, MouseWheelListener {

    private String figureName;
    public Shape shapeName;
    public Color currentColor;
    private String currentState = "start";
    private Point p;
    private Point q;
    private JFrame frame;
    private ArrayList<NamedShape> figuryArrayList = new ArrayList<>();
    private Polygon tempPolygon;
    private boolean isFirstDraw = true;
    private Serialization ser;


    private NamedShape shape;

    /**
     * Konstruktor klasy MyCanvas
     * @param frame
     */
    public MyCanvas(JFrame frame) {
        this.frame = frame;
        addMouseListener(this);
        addMouseMotionListener(this);
        this.setBorder(BorderFactory.createRaisedBevelBorder());
        //AffineTransform tx = new AffineTransform();
        ser = new Serialization();
        this.currentColor = Color.black;
        addMouseWheelListener(this);
    }


    /**
     * Funkcja rysująca figury
     * @param g
     */
    public void paintComponent(Graphics g){
        Graphics2D g2d = (Graphics2D) g;

        super.paintComponent(g);

        if(figuryArrayList.isEmpty() == false) {
            for (NamedShape s : figuryArrayList) {
                g2d.setColor(s.getColor());
                g2d.fill(s.getShape());
            }
        }



        //if(p == null || q == null) return;
        if(!(currentColor.equals(null))) g.setColor(currentColor);
        if(currentState.equals(Figury.DRAW.toString())) {
            if(p!=null && q!= null) {
                if (getFigureName() == "PROSTOKAT")
                    g.fillRect(Math.min(p.x, q.x), Math.min(p.y, q.y), Math.abs(q.x - p.x), Math.abs(q.y - p.y));
                else if (getFigureName() == "ELIPSA")
                    g.fillOval(Math.min(p.x, q.x), Math.min(p.y, q.y), Math.abs(q.x - p.x), Math.abs(q.y - p.y));
            }
            else if (getFigureName() == "WIELOKAT" && p!= null) g.fillPolygon(tempPolygon);
        }

        //System.out.println(getFigureName());
    }


    @Override
    public void mouseClicked(MouseEvent e) {
    }

    @Override
    public void mousePressed(MouseEvent e) {
        Point newPoint = new Point(e.getX(),e.getY());
        if(currentState.equals(Figury.KOLOR.toString())) {
            if(figuryArrayList.isEmpty() == false) {
                for(int i = figuryArrayList.size()-1; i >= 0; i--){
                    System.out.println(figuryArrayList.get(i).getShape());
                    if(figuryArrayList.get(i).getShape().contains(newPoint)){
                        System.out.println(figuryArrayList.get(i).getShape());
                        figuryArrayList.get(i).color = currentColor;
                        break;
                    }
                }
                frame.revalidate();
                frame.repaint();

//                if (tempShape != null) {
//                    tempShape.color = currentColor;
//                   // figuryArrayList.remove(new NamedShape(tempShape.getName(), tempShape.getShape(), tempShape.getColor()));
//                    //figuryArrayList.add(new NamedShape(tempShape.getName(), tempShape.getShape(), currentColor));
//                    frame.revalidate();
//                    frame.repaint();
//                }
            }
            else return;
        }
        else {
            if (figureName.equals(null)) return;
            p = new Point(e.getX(), e.getY());
            q = null;
            if (figureName.equals("WIELOKAT")) {
                tempPolygon.addPoint(p.x, p.y);

                frame.revalidate();
                frame.repaint();
            }
        }



    }

    @Override
    public void mouseReleased(MouseEvent e) {
        if(!(currentState.equals(Figury.DRAW.toString()))) return;
        else {
            if (q == null) return;
            if (getFigureName() == "PROSTOKAT") {
                shape = new NamedShape(getFigureName(), new Rectangle(Math.min(p.x, q.x), Math.min(p.y, q.y), Math.abs(q.x - p.x), Math.abs(q.y - p.y)), currentColor);
                figuryArrayList.add(shape);
            } else if (getFigureName() == "ELIPSA") {
                shape = new NamedShape(getFigureName(), new Ellipse2D.Double(Math.min(p.x, q.x), Math.min(p.y, q.y), Math.abs(q.x - p.x), Math.abs(q.y - p.y)), currentColor);
                figuryArrayList.add(shape);
            }
        }

    }

    @Override
    public void mouseEntered(MouseEvent e) {
    }

    @Override
    public void mouseExited(MouseEvent e) {

    }

    @Override
    public void mouseDragged(MouseEvent e) {



        if (currentState.equals(Figury.RESIZE.toString()) && q != null) {
            int dx = (int) (e.getX() - q.getX());
            int dy = (int) (e.getY() - q.getY());

            for (int i = figuryArrayList.size() - 1; i >= 0; i--) {
                // System.out.println(figuryArrayList.get(i).getShape());
                if (figuryArrayList.get(i).getShape().contains(q.getX(), q.getY())) {
                    //  System.out.println(figuryArrayList.ge1t(i).getShape());

                    AffineTransform tx = new AffineTransform();
                    tx.translate(dx,dy);
                    Shape newShape = tx.createTransformedShape(figuryArrayList.get(i).getShape());
                    figuryArrayList.get(i).setShape(newShape);
                    break;
                }
            }
        }

        if (getFigureName() != "WIELOKAT") q = new Point(e.getX(), e.getY());

        frame.revalidate();
        frame.repaint();
    }

    @Override
    public void mouseMoved(MouseEvent e) {

    }

    public String getFigureName() {
        return figureName;
    }

    public void setFigureName(String figureName) {
//        if(isFirstDraw == false) {
//            if (this.figureName.equals("WIELOKAT") && this.figureName != null) {
//                shape = new NamedShape(getFigureName(), tempPolygon, currentColor);
//                figuryArrayList.add(shape);
//            }
//        }
//        else isFirstDraw = false;
        this.figureName = figureName;
        if(this.figureName.equals(Figury.WIELOKAT.toString())){
            tempPolygon = new Polygon();
        }
    }

    @Override
    public void mouseWheelMoved(MouseWheelEvent e) {
        int x = e.getX();
        int y = e.getY();


        if(!(figureName.equals("WIELOKAT"))) {
            if (e.getScrollType() == MouseWheelEvent.WHEEL_UNIT_SCROLL) {

                if (figuryArrayList.isEmpty() == false) {
                    for (int i = figuryArrayList.size() - 1; i >= 0; i--) {
                        // System.out.println(figuryArrayList.get(i).getShape());
                        if (figuryArrayList.get(i).getShape().contains(x, y)) {
                            //  System.out.println(figuryArrayList.ge1t(i).getShape());
                            float amount = e.getWheelRotation() * (-1) * 0.05f + 1;

                            String shapeName = figuryArrayList.get(i).getName();

                            AffineTransform tx = new AffineTransform();
                            tx.scale(amount, amount);
                            double dx = figuryArrayList.get(i).getShape().getBounds().getCenterX();
                            double dy = figuryArrayList.get(i).getShape().getBounds().getCenterY();
                            Shape newShape = tx.createTransformedShape(figuryArrayList.get(i).getShape());
                            System.out.println(newShape);
                            figuryArrayList.get(i).setShape(newShape);
                            double dxx = figuryArrayList.get(i).getShape().getBounds().getCenterX();
                            double dyy = figuryArrayList.get(i).getShape().getBounds().getCenterY();
                            tx = new AffineTransform();
                            tx.translate(dx - dxx, dy - dyy);
                            Shape newShape2 = tx.createTransformedShape(figuryArrayList.get(i).getShape());



                            figuryArrayList.get(i).setShape(newShape2);
                            System.out.println("XD "+ figuryArrayList.get(i).getShape().getBounds().getLocation());
                            frame.repaint();
                            break;
                        }
                    }
                    frame.revalidate();
                    frame.repaint();

                }
            }
        }
    }

    public String getCurrentState() {
        return currentState;
    }

    /**
     * Metoda ustawiająca stan wykonywanej akcji
     * @param currentState
     */
    public void setCurrentState(String currentState) {
        this.currentState = currentState;

        if (this.figureName != null && this.figureName.equals("WIELOKAT")) {
            System.out.println("bbb");
            shape = new NamedShape(getFigureName(), tempPolygon, currentColor);
            figuryArrayList.add(shape);
            if(!(this.currentState.equals(Figury.DRAW.toString()))) this.figureName = "a";
        }

        if(this.currentState.equals("SAVE")) {
            try {
                ser.Save(figuryArrayList);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

        if(this.currentState.equals("LOAD")) {
            figuryArrayList = ser.Read();

            frame.revalidate();
            frame.repaint();
        }
    }
}

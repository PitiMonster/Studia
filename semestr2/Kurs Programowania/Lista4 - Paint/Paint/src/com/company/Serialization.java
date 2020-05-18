package com.company;

import com.google.gson.Gson;

import com.google.gson.reflect.TypeToken;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
//import org.json.simple.parser.JSONParser;


import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Klasa odpowiadająca za serializację danych
 */
public class Serialization extends JPanel {

    /**
     * Funkcja zapisująca dane do pliku .json
     * @param shapeList
     * @throws IOException
     * @throws JSONException
     */
    public void Save(ArrayList<NamedShape> shapeList) throws IOException, JSONException {
        Gson gson = new Gson();
        JSONArray array = new JSONArray();
        JSONObject object;
        System.out.println(shapeList);
        for(NamedShape s: shapeList) {
           // s.setShape(s.getShape());
            System.out.println(s.getShape());
            String json = gson.toJson(s);
            object = new JSONObject(json);
            array.put(object);
        }
        System.out.println(array);


        JFileChooser chooser = new JFileChooser();
        int retrieval = chooser.showSaveDialog(null);
        if(retrieval == JFileChooser.APPROVE_OPTION) {
            if(!(chooser.getSelectedFile().toString().contains(".json")))
                try(FileWriter fw = new FileWriter(chooser.getSelectedFile()+".json")){
                    fw.write(array.toString());
                }
            else
                try(FileWriter fw = new FileWriter(chooser.getSelectedFile())){
                    fw.write(array.toString());
                }
        }
    }


    /**
     * Funkcja wczytująca dane z pliku .json
     * @return
     */
    public ArrayList<NamedShape> Read() {
        JFileChooser chooser = new JFileChooser();
        ArrayList<NamedShape> namedShapes = new ArrayList<>();
        Gson gson = new Gson();
        NamedShape shape;

        int retrieval = chooser.showOpenDialog(null);
        if(retrieval == JFileChooser.APPROVE_OPTION) {

            try{
                FileReader fileReader = new FileReader(chooser.getSelectedFile());
                BufferedReader bufferedReader = new BufferedReader(fileReader);
                StringBuilder fileContent = new StringBuilder();
                String st;

                while((st = bufferedReader.readLine())!=null){
                    fileContent.append(st);
                }
                bufferedReader.close();

                JSONArray arr = new JSONArray(fileContent.toString());

                System.out.println(arr);

                for(int i =0; i< arr.length();i++){

                    JSONObject obj2 = (JSONObject) arr.get(i);
                    Color color = gson.fromJson(obj2.getString("color"), Color.class);
                    String name = gson.fromJson(obj2.getString("name"), String.class);

                    if(name.equals(Figury.PROSTOKAT.toString())){
                        Rectangle rect = gson.fromJson(obj2.getString("shape"), Rectangle.class);
                        System.out.println(rect);
                        shape = new NamedShape(name,rect,color);
                        namedShapes.add(shape);
                    }
                    else if(name.equals(Figury.ELIPSA.toString())){
                        Ellipse2D.Double elip = gson.fromJson(obj2.getString("shape"), Ellipse2D.Double.class);
                        //System.out.println(elip);
                        shape = new NamedShape(name,elip,color);
                        namedShapes.add(shape);
                    }
                    else {
                        Polygon poly = gson.fromJson(obj2.getString("shape"), Polygon.class);
                        shape = new NamedShape(name,poly,color);
                        namedShapes.add(shape);
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

        return namedShapes;
    }
}

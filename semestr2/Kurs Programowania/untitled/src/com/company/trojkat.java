package com.company;

public class trojkat {
    public double x,y,z;
    public trojkat(double a, double b) throws Exception{
        x = a;
        y = b;
        if(x <0 || y < 0)throw new Exception("A i B mają być dodatnie");
        z = Math.sqrt(x*x+y*y);
    }
    public double obwod(){
        return x+y+z;
    }
}

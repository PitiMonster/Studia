import jdk.nashorn.internal.runtime.Debug;
import sun.nio.cs.ext.MacThai;

public class Figury {


    public enum Figury1 implements iFigura{
        OKRĄG{

            public double pole() {
                return Math.PI*p*p;
            }

            public double obwod() {
                return 2*Math.PI*p;
            }
        },


        KWADRAT{
            public double pole() {
                return p*p;
            }

            public double obwod() {
                return p*4;
            }
        },
        PIĘCIOKĄT{
            public double pole() {
                return 5 / 4.0 * p * p / Math.tan(Math.PI / 5);
            }

            public double obwod() {
                return 5*p;
            }
        },
        SZCZEŚCIOKĄT{
            public double pole() {
                return 6 / 4.0 * p * p / Math.tan(Math.PI / 6);
            }

            public double obwod() {
                return 6*p;
            }
        };

        int p;

        public void setParametr(int p){
            this.p = p;
        }
    }

    public enum Figury2 implements iFigura{
        PROSTOKĄT{
            public double pole() {
                return p1*p2;
            }

            public double obwod() {
                return 2*p1+2*p2;
            }
        },
        ROMB{
            @Override
            public double pole() {
                return p1*p1*Math.sin(p2*Math.PI/180.0);
            }

            @Override
            public double obwod() {
                return 4*p1;
            }
        };

        int p1,p2;

        public void setParametr(int p1, int p2){
            this.p1 = p1;
            this.p2 = p2;
        }


   }



    public static void main(String[] args) {

        int iloscArgumentow = args.length;
        if(iloscArgumentow == 0) {
            System.out.println("Za malo danych");
            System.exit(0);
        }
        String typyFigur = args[0];
        iFigura [] figury = new iFigura[typyFigur.length()];
        int wskaznik = 0;

        for(int i = 0; i < typyFigur.length(); i++) {
            try {
                int znak = typyFigur.charAt(i);
                if (znak == 'o') {
                    if (wskaznik + 1 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int promien = Integer.parseInt(args[wskaznik+1]);

                    wskaznik ++;

                    Figury1 figura = Figury1.OKRĄG;
                    figura.setParametr(promien);
                    figury[i] = figura;
                    System.out.print("okrąg");


                }
                else if (znak == 'c') {
                    if (wskaznik + 5 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int bok1 = Integer.parseInt(args[wskaznik + 1]);
                    int bok2 = Integer.parseInt(args[wskaznik + 2]);
                    int bok3 = Integer.parseInt(args[wskaznik + 3]);
                    int bok4 = Integer.parseInt(args[wskaznik + 4]);
                    int kat = Integer.parseInt(args[wskaznik + 5]);

                    wskaznik += 5;

                    if(kat == 90){
                        if(bok1 == bok2 && bok2 == bok3 && bok3 == bok4) {

                            Figury1 figura = Figury1.KWADRAT;
                            figura.setParametr(bok1);
                            figury[i] = figura;
                            System.out.print("kwadrat");
                        }
                        else {
                            Figury2 figura = Figury2.PROSTOKĄT;
                            if(bok1 != bok2) figura.setParametr(bok1, bok2);
                            else figura.setParametr(bok1, bok3);
                            figury[i] = figura;
                        }
                    }
                    else {

                        Figury2 figura = Figury2.ROMB;
                        figura.setParametr(bok1, kat);
                        figury[i] = figura;
                    }

                }

                else if(znak == 'p') {
                    if (wskaznik + 1 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int bok = Integer.parseInt(args[wskaznik+1]);

                    wskaznik++;

                    Figury1 figura = Figury1.PIĘCIOKĄT;
                    figura.setParametr(bok);
                    figury[i] = figura;

                }

                else if(znak == 's') {

                    if (wskaznik + 1 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int bok = Integer.parseInt(args[wskaznik+1]);

                    wskaznik++;

                    Figury1 figura = Figury1.SZCZEŚCIOKĄT;
                    figura.setParametr(bok);
                    figury[i] = figura;

                }
            }
            catch(Exception e) {
                System.out.println(e);
            }
        }

        for(iFigura figura : figury) {
            if(figura != null)
                System.out.printf("Pole: %.2f Obwod: %.2f\n", figura.pole(), figura.obwod());
        }
    }
}




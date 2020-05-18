import sun.rmi.runtime.Log;

import static jdk.nashorn.internal.runtime.regexp.joni.Config.log;

public class figury {
    public static void main(String[] args) {

        int iloscArgumentow = args.length;
        if(iloscArgumentow == 0) {
            System.out.println("Za malo danych");
            System.exit(0);
        }
        String typyFigur = args[0];
        Figura [] figury = new Figura[typyFigur.length()];
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

                    figury[i] = new Kolo(promien);

                    wskaznik += 1;
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

                    if(kat == 90){
                        if(bok1 == bok2 && bok2 == bok3 && bok3 == bok4) figury[i] = new Kwadrat(bok1, bok2, bok3, bok4, kat);
                        else
                            figury[i] = new Prostokat(bok1, bok2, bok3, bok4, kat);
                    }
                    else
                        figury[i] = new Romb(bok1, bok2, bok3, bok4, kat);
                    wskaznik += 5;
                }

                else if(znak == 'p') {
                    if (wskaznik + 1 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int bok = Integer.parseInt(args[wskaznik+1]);

                    figury[i] = new Pieciokat(bok);
                    wskaznik++;
                }

                else if(znak == 's') {

                    if (wskaznik + 1 > iloscArgumentow) {
                        System.out.println("Za malo agrumentow");
                        System.exit(0);
                    }

                    int bok = Integer.parseInt(args[wskaznik+1]);

                    figury[i] = new Szesciokat(bok);
                    wskaznik++;
                }
            }
            catch(Exception e) {
                System.out.println(e);
            }
        }

        for(Figura figura : figury) {
            if(figura != null)
                System.out.printf("Pole: %.2f Obwod: %.2f\n", figura.pole(), figura.obwod());
        }
    }
}

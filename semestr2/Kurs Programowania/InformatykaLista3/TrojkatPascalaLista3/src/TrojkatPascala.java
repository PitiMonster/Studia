import com.sun.deploy.panel.JSmartTextArea;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


class WierszTrojkataPascala implements ActionListener {

        public static int [] wiersz;

        // tworzenie noweg okna
        static JFrame frame = new JFrame("Trojkat Pascala");
        static JPanel firstPanel = new JPanel();
        static JPanel secondPanel = new JPanel();

        // tworzenie nowego buttona ktory bedzie powodował wyświetlenie trójkąta
        static JButton buttonWypisz = new JButton("Wypisz trojkat");

        // tworzenie pola dla użytkownika w które wpisze rozmiar trójkata
        static JTextField amountField = new JTextField(15);

        // tworzenie nowego pola na wyswietlanie trojkata
        static JSmartTextArea textTrojkat;



    // kontruktor klasy który uzupelnia tabele wiersz
        public WierszTrojkataPascala() {


            // ustalenie romairu okna
           //frame.setSize(1500,2000);


            // wlaczanie opcji wylaczenia okna
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);



            // ustalenie wspolrzednych buttona
           // buttonWypisz.setBounds(700, 135, 115, 55);

            // rozmieszczenie amountText na plaszczyznie okna app
           // amountField.setBounds(700,70,115,30);

            JLabel ileWierszyLabel = new JLabel("<html><div style='text-align: center;'>" + "Liczba wierszy:" + "</div></html>");

            //ileWierszyLabel.setBounds(600, 70, 115, 30);

            firstPanel.add(ileWierszyLabel);

            // dodanie amountText do okna app
            firstPanel.add(amountField);

            //rejestrowanie buttona do action listenera
            buttonWypisz.addActionListener(this);

            // dodanie buttona do okna app
            firstPanel.add(buttonWypisz);

            frame.add(firstPanel);
            frame.pack();
            frame.setLocationRelativeTo(null);


            // pokazanie okna app na ekranie
            frame.setVisible(true);
        }

        // metoda wypisujaca konretny wspolczynnik
        public void Wspolczynnik(int m) {
            System.out.println(m + " - " + wiersz[m]);
        }

        public static void policzWiersz(int n ) {

            if(n<0) {
                System.out.println(n + " - niepoprawny numer wiersza");
                System.exit(0);
            }

            wiersz = new int[n+1];
            wiersz[0] = 1;
            wiersz[n] = 1;

            for(int i = 1; i <= n; i++) {

                wiersz[i] = wiersz[i-1] * (n-i+1) / i;
            }
        }


        //metoda wypisujaca trojkat
        public static void wypiszTrojkat(int liczbaWierszy) {
            textTrojkat = new JSmartTextArea();
            frame = new JFrame("Wiersz Trojkata Pascala");
            new WierszTrojkataPascala();


           // textTrojkat.setBounds(350,250,liczbaWierszy*50,liczbaWierszy*30);

            Font font = new Font("Scriptyca", Font.PLAIN, 20);
           // textTrojkat.setFont(font);
         //   textTrojkat.setBackground(Color.WHITE);
           // textTrojkat.setBorder(BorderFactory.createEtchedBorder());


            // dodaanie textTrojkat do okna app
         //   frame.add(textTrojkat);

            for(int i = 0; i < liczbaWierszy; i++) {
                policzWiersz(i);


                for(int j = 0; j < wiersz.length ; j++) {


                    textTrojkat.append(wiersz[j]+" ");
                }

                textTrojkat.append("<br>");


            }

           // frame.add(textTrojkat);
         //   textTrojkat.setVisible(true);
            JLabel label = new JLabel("<html><div style='text-align: center;'>" + textTrojkat.getText() + "</div></html>");
            //label.setBounds(710,250,1500,liczbaWierszy*30);
            secondPanel.add(label); 
           // secondPanel.setLayout(new GridLayout(liczbaWierszy, 1));
            firstPanel.setVisible(false);
            frame.remove(firstPanel);
            frame.add(secondPanel);

            label.setFont(font);
            label.setVisible(true);
            frame.pack();

            // pokazanie okna app na ekranie
            frame.setVisible(true);

        }


        //Overriding actionPerformed() method
        @Override
        public void actionPerformed(ActionEvent e) {
            try {

                int liczbaWierszy = Integer.parseUnsignedInt(amountField.getText());
                wypiszTrojkat(liczbaWierszy);
            }
            catch(NumberFormatException el) {

            }

        }

        public static void main(String[] args) {

            new WierszTrojkataPascala();



            }

//            try {
//                int n = Integer.parseInt(args[0]);
//                wypiszTrojkat(n);
//            }
//            catch(NumberFormatException ex) {
//                System.out.println(args[0] + " - niepoprawny numer wiersza");
//                System.exit(0);
//            }

//            for(int i = 1; i < args.length; i++) {
//                try {
//                    int m = Integer.parseInt(args[i]);
//                    if(m >= 0  && m < wiersz.length) Wspolczynnik(m);
//                    else {
//                        System.out.println(m + " - liczba spoza zakresu");
//                    }
//                }
//                catch(NumberFormatException ex) {
//                    System.out.println(args[i] + " - niepoprawna dana");
//                }
//
//            }




}


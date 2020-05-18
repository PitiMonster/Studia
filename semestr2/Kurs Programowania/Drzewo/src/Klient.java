import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Klient {

    public static void main(String[] args){

        //Tworzenie gniazda, i sprawdzenie czy host/pory serwera nasłuchuje
        String host;
        int port;
        Scanner scanner = new Scanner(System.in);


        if(args.length==0){
            host= "localhost";
            port = 999;
        }
        else{
            host = args[0];
            String portStr = args[1];
            try {
                port=Integer.parseInt(portStr);
            }
            catch(NumberFormatException nfe){
                System.out.println("Uuups, zły numer portu. Przełączam na domyslny port: 9999");
                port = 999;
            }
        }
        try{
            //Próba połączenia z serwerem
            System.out.println("Klient: Próba podłączenia do serwera jako host-"+host+" port: "+port+'.');
            Socket skt = new Socket(host,port);

            //Opcje odczytu i zapisu z i do strumienia
            BufferedReader Input = new BufferedReader(new InputStreamReader(skt.getInputStream())); //odczyt

            String command;


            while(true){
                command = scanner.nextLine();

                PrintWriter out = new PrintWriter(skt.getOutputStream(),true);
                out.println(command);
                out.flush();

                //Sprawdzenie, czy serwer odpowiedział.
                String buf=Input.readLine();
                if(buf !=null){
                    System.out.println("Klient: Odpowiedź serwera [ "+buf+" ]");
                    if(buf.equals("do zobaczenia!")) {
                        out.flush();
                        skt.close();
                    }
                }
                else
                    System.out.println("Klient: Brak odpowiedzi z serwera.");
            }

            //Przesłanie sprawdzającej wiadomości na serwer:




////            // Zamknięcie połączenia ze strony klienta
////
////            System.out.println("Klient - Odłączony");

        }
        catch (IOException ex){
            ex.printStackTrace();
            System.out.println("Uuuups, coś się skopało. nie podziałam!");
        }
    }
}
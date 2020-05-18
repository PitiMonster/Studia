import java.io.*;
import java.net.*;

public class Server {

    public static void main(String[] args) throws ClassNotFoundException {
        // TODO Auto-generated method stub
        // tworzenie stringa na przechowywanie rozdzielonych komend
        String[] stringArray;
        // tworzenie poczatkowego drzewa typu Integer
        Tree<Integer> intTree = new Tree<>();
        Tree<Double> doubleTree = new Tree<>();
        Tree<String> stringTree = new Tree<>();

        // aktualny typ drzewa
        String typDrzewa = "Integer";

        Class<?> theClass = Class.forName("java.lang.Integer");

        try{
            ServerSocket myServerSocket = new ServerSocket(999); //stworzenie gniazda servwera i przypisanie mu portu (tu 9999)

            // Oczekiwanie na połączenie od hosta
            System.out.println("Serwer: Start na hoście-"
                    +InetAddress.getLocalHost().getCanonicalHostName()
                    +" port: "+myServerSocket.getLocalPort());
            Socket skt = myServerSocket.accept();

            //Opcje odczytu i zapisu z i do strumienia
            BufferedReader Input = new BufferedReader(new InputStreamReader(skt.getInputStream())); //odczyt
            PrintStream Output = new PrintStream(skt.getOutputStream());                            //zapis

            while(true) {
                //Próba odczytania wejścia ze strumienia
                String buf = Input.readLine();

                //Sprawdzenie, czy serwer odebrał wiadomość i próba odpisania hostowi
                if (buf != null) {
                    stringArray = buf.split(" ");
                    PrintWriter out = new PrintWriter(skt.getOutputStream(),true);
                    // zmiana typu drzewa
                    if(stringArray[0].equals("zmien") && stringArray[1].equals("typ")){
                        if(stringArray[3].equals("Integer")) {
                            intTree = new Tree<>();
                            out.println("zmieniono pomyslnie");
                            typDrzewa = stringArray[3];
                        }
                        else if(stringArray[3].equals("Double"))  {
                            doubleTree = new Tree<>();
                            out.println("zmieniono pomyslnie");
                            typDrzewa = stringArray[3];
                        }
                        else if(stringArray[3].equals("String")) {
                            stringTree = new Tree<>();
                            out.println("zmieniono pomyslnie");
                            typDrzewa = stringArray[3];
                        }
                        else out.println("Niestety nie obslugujemy takiego typu danych");
                    }
                    // wywowlanie inserta
                    else if (stringArray[0].equals("insert")) {

                        if(typDrzewa.equals("Integer")) {
                            intTree.insert(Integer.parseInt(stringArray[1]));
                            out.println(intTree.toString());
                        }
                        else if(typDrzewa.equals("Double")) {
                            doubleTree.insert(Double.parseDouble(stringArray[1]));
                            out.println(doubleTree.toString());
                        }
                        else {
                            stringTree.insert(stringArray[1]);
                            out.println(stringTree.toString());
                        }
                    }
                    // wywolanie szukania elementu
                    else if(stringArray[0].equals("search")){
                        if(typDrzewa.equals("Integer")) {
                            if(intTree.isElement(Integer.parseInt(stringArray[1])) == true) out.println("Element jest w drzewie");
                            else out.println("Elementu nie ma w drzewie");
                        }
                        else if(typDrzewa.equals("Double")) {
                            if(doubleTree.isElement(Double.parseDouble(stringArray[1])) == true) out.println("Element jest w drzewie");
                            else out.println("Elementu nie ma w drzewie");
                        }
                        else {
                            if(stringTree.isElement(stringArray[1]) == true) out.println("Element jest w drzewie");
                            else out.println("Elementu nie ma w drzewie");
                        }
                    }
                    // wywolanie usuniecia elementu
                    else if(stringArray[0].equals("delete")){
                        if(typDrzewa.equals("Integer")) {
                            if(intTree.isElement(Integer.parseInt(stringArray[1])) == true) intTree.delete(Integer.parseInt(stringArray[1]));
                            else out.println("Elementu nie ma w drzewie");
                            out.println(intTree.toString());
                        }
                        else if(typDrzewa.equals("Double")) {
                            if(doubleTree.isElement(Double.parseDouble(stringArray[1])) == true) doubleTree.delete(Double.parseDouble(stringArray[1]));
                            else out.println("Elementu nie ma w drzewie");
                            out.println(doubleTree.toString());
                        }
                        else {
                            if(stringTree.isElement(stringArray[1]) == true) stringTree.delete(stringArray[1]);
                            else out.println("Elementu nie ma w drzewie");
                            out.println(stringTree.toString());
                        }
                    }
                    // wywolanie funkcji draw
                    else if(stringArray[0].equals("draw")){
                        if(typDrzewa.equals("Integer")) out.println(intTree.toString());
                        else if(typDrzewa.equals("Double")) out.println(doubleTree.toString());
                        else out.println(stringTree.toString());
                    }
                    // zamkniecie polaczenia ze strony klienta
                    else if(buf.equals("koniec")) out.println("do zobaczenia!");
                    else out.println("takiej komendy nie obslugujemy");
                    System.out.println("Serwer, odczyt: [ " + stringArray[0] + " ]");
                    // zakonczenie pracy gry
                    if (buf.equals("koniec")) {
                        out.println("do zobaczenia!");
                    }
                    //out.println("elo");
                    out.flush();
                    //Output.print("Serwer: No siemka!"); //Odpowiedź dla hosta w przypadku odebrania wiadomości
                }
                // Zamknięcie połączenia ze strony serwera
                //skt.close();
                //System.out.println("Serwer - Odłączony");
            }

        }
        catch (IOException ex){
            ex.printStackTrace();
            System.out.println("Uuuups, coś się skopało. nie podziałam!");
        }
    }

}
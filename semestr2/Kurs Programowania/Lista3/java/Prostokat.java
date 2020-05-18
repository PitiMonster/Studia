public class Prostokat extends Czworokat {

    public Prostokat(int bok1, int bok2, int bok3, int bok4, int kat) throws Exception {
        super(bok1, bok2, bok3, bok4, kat);

        if(kat != 90)
            throw new Exception("zly kat");
    }
}



public class Romb extends Czworokat {

    private int bok1, bok2, bok3, bok4, kat;

    @Override
    public double pole() {
        return bok1 * bok2 * Math.sin(kat*Math.PI/180);
    }

    @Override
    public  double obwod() {
        return bok1 + bok2 + bok3 + bok4;
    }

    public Romb(int bok1, int bok2, int bok3, int bok4, int kat) throws Exception {
        if(!(bok1 == bok2 || bok2 == bok3 || bok3 == bok4))
            throw new Exception("niepoprawny rozmiar bokow");
        if(kat <= 0 || kat >= 180)
            throw new Exception("niepoprawny kat");

        this.bok1 = bok1;
        this.bok2 = bok2;
        this.bok3 = bok3;
        this.bok4 = bok4;
        this.kat = kat;
    }
}

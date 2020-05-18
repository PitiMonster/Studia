
public class Prostokat extends Czworokat {

    private int bok1, bok2, bok3, bok4, kat;

    @Override
    public double pole() {
        if(bok1 == bok2) return bok1 * bok3 * Math.sin(kat*Math.PI/180);
        else  return bok1 * bok2 * Math.sin(kat*Math.PI/180);
    }

    @Override
    public  double obwod() {
        return bok1 + bok2 + bok3 + bok4;
    }

    public Prostokat(int bok1, int bok2, int bok3, int bok4, int kat) throws Exception {
        if(bok1 <= 0 || bok2 <= 0 || bok3 <= 0|| bok4 <= 0)
            throw new Exception("niedodatnie boki");
        if(kat != 90)
            throw new Exception("zly kat");

        this.bok1 = bok1;
        this.bok2 = bok2;
        this.bok3 = bok3;
        this.bok4 = bok4;
        this.kat = kat;
    }
}

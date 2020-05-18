

public class Pieciokat extends Figura {

    private int bok;

    @Override
    public double pole() {
        return 5 / 4.0 * bok * bok / Math.tan(Math.PI / 5);
    }

    @Override
    public double obwod() {
        return 5 * bok;
    }


    public Pieciokat(int bok) throws Exception{
        if(bok <= 0)
            throw new Exception("niedodatni bok");

        this.bok = bok;
    }
}

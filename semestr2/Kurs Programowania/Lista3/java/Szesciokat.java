public class Szesciokat extends Figura{

    private int bok;

    @Override
    public double pole() {
        return 6 / 4.0 * bok * bok / Math.tan(Math.PI / 6);
    }

    @Override
    public double obwod() {
        return 6 * bok;
    }


    public Szesciokat(int bok) throws Exception{
        if(bok <= 0)
            throw new Exception("niedodatni bok");

        this.bok = bok;
    }

}

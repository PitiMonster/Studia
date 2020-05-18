

public class Kolo extends Figura{

    private int promien;

    @Override
    public double pole() {
        return promien*promien*Math.PI;
    }

    @Override
    public double obwod() {
        return 2*Math.PI*promien;
    }

    public Kolo(int promien) throws Exception {
        if(promien <= 0 )
            throw new Exception("Blad: niedodatni promien");

        this.promien = promien;
    }
}

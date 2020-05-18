#include <iostream>
#include <math.h>
#include <cstdio>
#include <vector>
#include <locale>
#include <sstream>
#define PI 3.14159265
using namespace std;
class Figura
{
public:
    virtual float pole() = 0;
    virtual float obwod() = 0;
    string nazwa;
};
class Kolo : public Figura
{
public:

    int promien;
    Kolo(int r)
    {
        promien = r;
        nazwa = "kolo";
    }
    float pole()
    {
        return PI * promien*promien;
    }
    float obwod()
    {
        return PI * 2 * promien;
    }
};
class Czworokat : public Figura
{
public:
    float bok1 = 0, bok2 = 0, bok3 = 0, bok4 = 0;
    int kat = 0;
    Czworokat(int boka, int bokb, int bokc, int bokd, int k)
    {
        bok1 = boka;
        bok2 = bokb;
        bok3 = bokc;
        bok4 = bokd;
        kat = k;
    }
    float obwod()
    {
        return bok1 + bok2 + bok3 + bok4;
    }

};
class Kwadrat : public Czworokat
{
public:
    Kwadrat(int boka, int bokb, int bokc, int bokd, int k) : Czworokat(boka,bokb,bokc,bokd,k)
    {
        nazwa = "kwadrat";
    }
    float pole()
    {
        return bok1 * bok1;
    }


};
class Romb : public Czworokat
{
public:
    Romb(int boka, int bokb, int bokc, int bokd, int k) : Czworokat(boka, bokb, bokc, bokd, k)
    {
        nazwa = "romb";
    }
    float pole()
    {
        return bok1 * bok1*sin(kat*PI / 180);
    }

};
class Prostokat : public Czworokat
{
public:
    Prostokat(int boka, int bokb, int bokc, int bokd, int k) : Czworokat(boka, bokb, bokc, bokd, k)
    {
        nazwa = "prostokat";
    }
    float pole()
    {
        if (bok1 == bok2)
            return bok1 * bok3;
        else
            return bok1 * bok2;
    }

};
class Pieciokat : public Figura {
public:
    int bok;
    Pieciokat(int b)
    {
        bok = b;
        nazwa = "pieciokat";
    }
    float pole()
    {
        return (float) ( ((bok*bok)* sqrt(25+10*sqrt(5)))/4 );
    }
    float obwod()
    {
        return 5*bok;
    }



};
class Szesciokat : public Figura {
    public:
    int bok;
     Szesciokat(int b) {
        bok = b;
        nazwa = "Szesciokat";
    }
     float pole() {
        return (float)((3*bok*bok*sqrt(3))/2);
    }
     float obwod() {
        return 6*bok;
    }
};
int zamien(string a)
{
    int k = 0;
    for (int i = 0; i < a.size(); i++)
    {
        k *= 10;
        if (!isdigit(a[i]))
        {
            return -1;
        }
        k += (int)(a[i] - '0');
    }
    return k;
}
bool dodatnia(int a[5])
{
    for(int i = 0; i<5; i++)
    {
        if(a[i]<=0)return false;
    }
    return true;
}
int main(int max_pozycja, char *argv[])
{
    vector <Figura*> figury;
    string args = argv[1];
    int pozycja = 2;
    max_pozycja--;
    for (int i = 0; i < args.size(); i++)
    {

        char c = args[i];
        if (c == 'o')
        {
            if (pozycja > max_pozycja)
            {
                cout<<"Figura numer "<< i << " Koniec danych!\n";
            }
            else
            {
                Kolo *kolo = new Kolo(zamien(argv[pozycja]));
                if (kolo->promien <= 0)
                    cout<<"Figura numer "<< i << " - niepoprawnie podane dane\n";
                else
                    figury.push_back(kolo);
                pozycja++;
            }
        }
        if(c=='p')
        {
            if(pozycja > max_pozycja)
            {
                cout<<"Figura numer " << i << " Koniec danych!\n";
            }
            else
            {
                Pieciokat *pieciokat = new Pieciokat(zamien(argv[pozycja]));
                pozycja++;
                if(pieciokat->bok <= 0)
                    cout<<"Figura numer " << i << " - niepoprawnie podane dane\n";
                else
                    figury.push_back(pieciokat);
            }
        }
        if(c=='s')
        {
            if(pozycja > max_pozycja)
            {
                cout<<"Figura numer " << i << " Koniec danych!\n";
            }
            else
            {
                Szesciokat *szesciokat = new Szesciokat(zamien(argv[pozycja]));
                pozycja++;
                if(szesciokat->bok <= 0)
                    cout<<"Figura numer " << i << " - niepoprawnie podane dane\n";
                else
                    figury.push_back(szesciokat);
            }
        }
           if(c=='c') {
                if(pozycja + 4 > max_pozycja) {
                    cout<<"Figura numer " << i << " Koniec danych!\n";
                }
                else {


                    int b[5];
                    for (int k = 0; k < 5; k++) {
                        b[k] = zamien(argv[pozycja]);
                        pozycja++;
                    }
                    if (!dodatnia(b)) {
                        cout<<"Figura numer " << i << " - niepoprawnie podane dane\n";
                    } else {
                        if (b[0] == b[1] && b[0] == b[2] && b[0] == b[3]) {
                            if (b[4] == 90) {
                                Kwadrat *kwadrat = new Kwadrat(b[0], b[1], b[2], b[3], b[4]);
                                figury.push_back(kwadrat);
                            } else if (b[4] < 180 && b[4] > 0) {
                                Romb *romb = new Romb(b[0], b[1], b[2], b[3], b[4]);
                                figury.push_back(romb);
                            }
                        } else if (((b[0] == b[1] && b[2] == b[3]) || (b[0] == b[2] && b[3] == b[1]) || (b[0] == b[3] && b[1] == b[2])) && b[4] == 90) {
                            Prostokat *prostokat = new Prostokat(b[0], b[1], b[2], b[3], b[4]);
                            figury.push_back(prostokat);
                        } else cout<<"Figura numer " << i << " - niepoprawnie podane dane\n";
                    }


                }
            }
    }
    for(int i =0; i<figury.size(); i++)
    {
        cout << figury[i]->nazwa << " obwod: " << figury[i]->obwod() << " pole: " << figury[i]->pole()<<'\n';
    }
    return 0;
}


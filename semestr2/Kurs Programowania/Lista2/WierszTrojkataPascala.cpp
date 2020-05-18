#include <iostream>
#include <string.h>
#include <cstring>


using namespace std;

int* wiersz;

class WierszTrojkataPascala {
	
public:
	void correctValue(int n) {
		if (n < 0) {
			cout << n << " - niepoprawny numer wiersza" << '\n';
			exit(0);
		}
		else {
			wiersz = new int[n + 1000];
		}
	}

	void fillAnArray(int n) {
		wiersz[0] = 1;
		wiersz[n] = 1;

		for (int i = 1; i <= n; i++) {
			wiersz[i] = wiersz[i - 1] * (n - i + 1) / i;
		}
	}

	void Wspolczynnik(int m) {
		cout <<m<<" - "<<wiersz[m] <<'\n';
	}

	bool czyLiczba(string wyraz) {
		for (int i = 0; i < wyraz.length(); i++) {
			if (wyraz[i] < '0' || wyraz[i] > '9') return false;
		}
		return true;
	}

};



int main(int argc, char** argv)
{
	WierszTrojkataPascala trojkat;
	int n;

	if(trojkat.czyLiczba(argv[1]) == true) {
		n = stoi(argv[1]);
		trojkat.correctValue(n);
	}
	else {
		cout << argv[1] << " - niepoprawny numer wiersza" << "\n";
		exit(0);
	}

	trojkat.fillAnArray(n);

	for (int i = 2; i <= argc; i++)
	{
		if (trojkat.czyLiczba(argv[i]) == true) {
			int m =stoi(argv[i]);

			if (m >= 0 && m < sizeof(wiersz)+2) trojkat.Wspolczynnik(m);
			else {
				cout << m << " - liczba spoza zakresu" << "\n";
			}
		}
		else {
			cout << argv[i] << " - niepoprawny typ danych" << "\n";
		}
	}

	delete wiersz;
}
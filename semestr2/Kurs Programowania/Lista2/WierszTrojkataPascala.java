public class WierszTrojkataPascala {
	
	public static int [] wiersz;

	public WierszTrojkataPascala(int n) {
		
		if(n<0) {
			System.out.println(n + " - niepoprawny numer wiersza");
			System.exit(0);
		}		
		
		wiersz = new int[n+1];
		wiersz[0] = 1;
		wiersz[n] = 1;

		for(int i = 1; i <= n; i++) {
		
			wiersz[i] = wiersz[i-1] * (n-i+1) / i;
		}
	}

	public static void Wspolczynnik(int m) {
		System.out.println(m + " - " + wiersz[m]);
	}
		


	public static void main(String[] args) {
		try {
			int n = Integer.parseInt(args[0]);
			WierszTrojkataPascala newWiersz = new WierszTrojkataPascala(n);
		}	
		catch(NumberFormatException ex) {
			System.out.println(args[0] + " - niepoprawny numer wiersza");
			System.exit(0);
		}

		for(int i = 1; i < args.length; i++) {
			try {
				int m = Integer.parseInt(args[i]);
				if(m >= 0  && m < wiersz.length) Wspolczynnik(m);
				else {
					System.out.println(m + " - liczba spoza zakresu");
			}
			}	
			catch(NumberFormatException ex) {
				System.out.println(args[i] + " - niepoprawna dana");
			}
			
		}			
		
	}
}
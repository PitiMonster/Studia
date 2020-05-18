public class zad3 {
	
	private static int n;

	public static int div(int n) {
		for(int i = n-1; i >= 1; i--) {
			if(n%i == 0) {
				System.out.println(n + " " + i);
				return 0;
			}
		}
		return 0;
	}

	public static void main(String[] args) {
		for(int i = 0; i < args.length; i++) {
			try { 
				n=Integer.parseInt(args[i]);
				div(n);
			}
			catch (NumberFormatException ex) {
				System.out.println(args[i] + " nie jest liczba calkowita");
			}
			
		}
	}
}
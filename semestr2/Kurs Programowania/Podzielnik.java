public class Podzielnik
{
	public static int div(int n)
	{
		for(int i = n/2; ; i--)
		{
			if(n%i == 0)
			{
				return i;
			}
		}
	}	

	public static void main(String[] args)
	{
		int n = 0;
		for(int i = 0; i < args.length; i++)
		{
			try { n=Integer.parseInt(args[i]); }
			catch (NumberFormatException ex) {
				System.out.println(args[i] + " nie jest liczba calkowita");
				continue;
			}

			if(n<0)
			{
				System.out.println("Podana liczba jest ujemna");
			}
			else
			{
				System.out.println("Najwiekszym dzielnikiem " + n + " jest " + div(n));
			}
		}

	}
}

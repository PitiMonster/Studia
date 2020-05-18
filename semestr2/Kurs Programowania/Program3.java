public class Program3 
{


	public static int div(int n)
	{
		for(int i = 2; ; i++)
		{
			if(n%i == 0)
			{
				return n/i;
			}
		}
	}	


	public static void main(String[] args)
	{
		int n=0;
		for(int i = 0; i < args.length; i++) 
		{
			try{n=Integer.parseInt(args[i]); 
				if(n==0)
				{
					System.out.println("niepoprawny input");
				} 
				else if(n<0)
				{
					n = n*(-1);
					System.out.println("Najwiekszym dzielnikiem jest " + div(n));
				}
				else
				{
					System.out.println("Najwiekszym dzielnikiem jest " + div(n));
				}
			}
			catch(NumberFormatException ex) 
			{
				System.out.println(args[i] + " nie jest liczba calkowita");
			}

		}

	}
}

			

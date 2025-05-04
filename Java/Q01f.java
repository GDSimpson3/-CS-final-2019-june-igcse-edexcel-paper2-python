package q01f;

public class Q01f
{
    public static void main(String[] args)
	{
        int [][] list_1f  = { { 2010, 8 }, { 4800, 11 }, { 2011, 4 }, { 5000, 9 } };
        double assistantSalary = 1000.00;
        
        for (int i =0; i<4; i++)
		{
            int shopIncome = list_1f[i][0];
            int assistantSales = list_1f[i][1];
            
            System.out.println("Shop income: " + shopIncome + " Assistant sales: " + assistantSales);

            if (  )
                { 
                    System.out.println("Assistant bonus = " + assistantSalary * 0.1);
                }

            else if (   )
                {
                    System.out.println("Assistant bonus = " + assistantSalary * 0.05);
                }

            else
                {
                    System.out.println("Assistant bonus = " + 0);
                }
        }
    }
}
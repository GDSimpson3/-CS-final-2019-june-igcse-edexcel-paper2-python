using System;

namespace Q01f
{
    class Q01f
    {
        static void Main(string[] args)
        {
            int[,] list_1f = { { 2010, 8 }, { 4800, 11 }, { 2011, 4 }, { 5000, 9 } };
            double assistantSalary = 1000.00;

            for (int i = 0; i<4; i++)
            {
                int shopIncome = list_1f[i, 0];
                int assistantSales = list_1f[i, 1];

                Console.WriteLine("Shop income: " + shopIncome + " Assistant sales: " + assistantSales);

                if (  )
                { 
                    Console.WriteLine("Assistant bonus = " + assistantSalary * 0.1);
                }

                else if (  )
                {
                    Console.WriteLine("Assistant bonus = " + assistantSalary * 0.05);
                }

                else
                {
                    Console.WriteLine("Assistant bonus = " + 0);
                  
                }
                    
            }

            Console.ReadLine();
        }
    }
}

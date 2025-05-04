using System;

namespace Q02c
{
	class Q02c
	{
		private static string amendMessage(string inMessage, int startPosition, int characters)
		{
			string outMessage = inMessage.Substring(startPosition, characters);
			return outMessage;
		}

		public static void Main(string[] args)
		{
			int check = 0;
			while (check == 0)
			{
				Console.Write("Enter a phrase, 'end' to finish: ");
				string message = Console.ReadLine();
				if (message == "end")
				{
					check = 1;
					Console.WriteLine("Goodbye");
					Console.ReadLine();
				}
				else 
				{
					Console.Write("Start position: ");
					int pos = Convert.ToInt16(Console.ReadLine());
					Console.Write("Number of characters: ");
					int characters = Convert.ToInt16(Console.ReadLine());
					string newMessage = amendMessage(message,pos,characters);
					Console.WriteLine("Thank you");
				}
			}
		}
	}
}
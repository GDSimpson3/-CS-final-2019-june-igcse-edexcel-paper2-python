package Q02c;

import java.util.Scanner;

public class Q02c
{
    private static String amendMessage(String inMessage, int startPosition, int characters)
	{
        String outMessage = inMessage.substring(startPosition, startPosition + characters);
        return outMessage;
	}

    public static void main(String[] args)
	{
        int check = 0;
		while (check == 0)
		{
            Scanner input = new Scanner(System.in);
            System.out.print("Enter a phrase, 'end' to finish: ");
            String message = input.nextLine();
            if (!"end".equals(message))
            {
                System.out.print("Start position: ");
                int pos = input.nextInt();
                System.out.print("Number of characters: ");
                int characters = input.nextInt();
                String newMessage = amendMessage(message,pos,characters);
                System.out.println("Thank you");               
            }
            else 
            {
                check = 1;
                System.out.println("Goodbye");
            }
        }
    }
}

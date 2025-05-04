package Q02b;

public class Q02b
{
    public static void main(String[] args)
	{
        double time = 0;
        double initialSpeed = 5;
        double acceleration = 2;
        double newSpeed = 0;
        double distance = 0;

        while (time < 4)
		{ 
            newSpeed = initialSpeed + time * acceleration;
            distance = 0.5 * time * (newSpeed + initialSpeed);
            time = time + 1;
		}
    }
}

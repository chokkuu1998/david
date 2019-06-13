ublic class SeperateNumbers // Start of class Seperate Numbers
{
public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
	int Number, temp;
	int var1, var2, var3, var4,var5;
	System.out.print("Enter a Five Digit Number: ");
	Number = input.nextInt();
	var1 = Number/10000;
	temp = Number% 10000;
	var2 = temp/1000;
	temp = Number%1000;
	var3 = temp/100;
	temp = Number% 100;
	var4 = temp/10;
	temp = Number%10;
	var5 = temp;
	System.out.println(var1);
	System.out.println(var2);
	System.out.println(var3);
	System.out.println(var4);
	System.out.println(var5);
	}

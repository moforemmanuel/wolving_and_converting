import java.util.*;

public class Convert {

	String ToHex(int decimalNumber) {

	    //numberSystem = 16;
		if(decimalNumber >= 0 && decimalNumber < 127) {
	    String hexa = "";
	    while(decimalNumber >= 16)
	    {
	      hexa += getHexa(decimalNumber % 16);
	      decimalNumber /= 16;
	    }
	    hexa += getHexa(decimalNumber);
	    return hexa;
		}
		else {
			return Integer.toHexString(decimalNumber);
		}
	  }
	
	  static String getHexa(int n)
	  {
	    String[] nums = {"0", "1","2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C","D", "E", "F"};
	    return nums[n];
	  }

	
	String ToOct(int decimalNumber) {
		
		//numberSystem = 8;
		if (decimalNumber >= 0 && decimalNumber < 127) {
	    String octal = "";
	    while(decimalNumber >= 8)
	    {
	      octal += decimalNumber % 8;
	      decimalNumber /= 8;
	    }
	    octal += decimalNumber;
	    return octal;
	    }
		else {
			return Integer.toOctalString(decimalNumber);
		}
	  }
	

	String ToBin(int decimalNumber) {
	
		//numberSystem = 2;
		if(decimalNumber >= 0 && decimalNumber < 127) {
	    String binary = "";
	    while(decimalNumber >= 2)
	    {
	      binary += decimalNumber % 2;
	      decimalNumber /= 2;
	    }
	    binary += decimalNumber;
	    return binary; 
		}
		else {
			return Integer.toBinaryString(decimalNumber);
		}
	}
	
	/*boolean validate(int decimalNumber) {
		if(decimalNumber < -128 && decimalNumber > 127) {
			System.out.println("Invalid input ...");
			return false;
		}
		else {
		return true;
		}
	}*/
	
	public static  void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		Convert convert = new Convert();
		while (true) {
			System.out.println("To convert a decimal to HEX, please type '1' and hit enter.\n" + 
				"To convert a decimal to OCT, please type '2' and hit enter.\n" + 
				"To convert a decimal to Binary, please type '3' and hit enter.\n" +
				"To quit, please type '4' and hit enter \n");
		
			int choice = scan.nextInt();
		
			if (choice == 1 || choice == 2 || choice == 3) {
				System.out.println("\nPlease enter the decimal number you wish to convert ... \n");
				int decimal = scan.nextInt();
				//boolean test = convert.validate(decimal);
				
				if (decimal >= -128 && decimal <= 127) {
					switch(choice) {
					
					case 1: {
						String HEX = convert.ToHex(decimal);
						System.out.println("\nThe hexadecimal representation of " + decimal +
								" is: " + HEX + " \n");
						break;
					}
					
					case 2: {
						String OCT = convert.ToOct(decimal);
						System.out.println("\nThe octal representation of " + decimal +
								" is: " + OCT + " \n");
						break;
					}
					
					case 3: {
						String BIN = convert.ToBin(decimal);
						System.out.println("\nThe binary representation of " + decimal +
								" is: " + BIN + " \n");
						break;
					}
					
					default:
						System.out.println("\n... Invalid Operation...\n");
						break;
				}
					//end of switch
				
			}//end if
			else {
				System.out.println("\n... Error : The number you input is out of range [-128,127] ...\n"+
			"... Please input a number greater than or equal to  -128 and less than or equal to 127 ...\n");
			}
		}
			//end choice if
			else if (choice == 4) {
				scan.close();
				System.out.println("... Good bye ... ");
				break;
			}
			else {
				System.out.println("\n... Error: Invalid Operation ...\n" +
			"... Please enter a valid operation by choosing 1, 2, 3, or 4 ...\n");
			}
	}
		//end while
}
	//end main
}
//end class
	


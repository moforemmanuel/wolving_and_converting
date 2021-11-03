"""
Wolving bank simple and compound interest calculator
"""

#program constants
PERIOD = 4 #number of compounding periods

def print_intro():
    """Prints the welcome message at start up"""

    print("Welcome to the Wolving compound interest calculator.")
    print("This program calculates your potential returns when you invest with us")

def get_input():
    """Returns the input of necessary data, obtained from user, to calculate the interest"""

    principal = int(input("How much would you like to invest? "))
    #get principal amount
    rate = float(input("What is the interest rate on your account? "))
    rate /= 100
    #get annual interest rate
    years = int(input("How long are you planning to invest (in years)? "))
    #get years of investment

    return principal, rate, years


def simple_interest(principal, rate, years):
    """Return the simple interest"""

    simple_amount = principal*(1 + (rate*years))
    #calculate simple interest
    return simple_amount

def compound_interest(principal, rate, years):
    """Return the calculated compound interest"""

    compound_amount = principal*((1 + (rate/PERIOD))**(PERIOD*years))
    #calculate compound interest
    return compound_amount

def print_output_compounding(principal, rate, years, simple_amount):
    """Prints formatted output of simple interest"""

    print("\n{}{} invested at {}% for {} years is: {}{:.2f}"\
    .format(chr(163), principal, rate*100, years, chr(163), simple_amount))

def print_compounding_output(principal, rate, years, compound_amount):
    """Prints formatted output of compound interest"""

    print("\n{}{} invested at {}% for {} years compounded {} times per year is: {}{:.2f}\n"\
    .format(chr(163), principal, rate*100, years, PERIOD, chr(163), compound_amount))

def get_target_input():
    """Return user target amount"""

    principal = int(input("How much would you like to invest? "))
    #get principal amount
    rate = float(input("What is the interest rate on your account? "))
    rate /= 100
    #get annual interest rate
    target = int(input("What is your savings goal? "))
    #get target amount


    return principal, rate, target


def calculate_years_to_target(principal, rate, target):
    """Return years expected to reach user target amount"""

    year = 1
    while year > 0:
        for i in range(1, 5):
            amount = compound_interest(principal, rate, 1)
            if amount >= target:
                break
            principal = amount
            i += 1
            year += 1
        if amount >= target:
            break
    return year

def print_target_output(principal, rate, years):
    """Prints the number of years taken to reach user target amount at a given rate"""

    print("\n{}{} invested at {}% will allow you to reach your savings target in {} years\n"\
    .format(chr(163), principal, rate*100, years))


if __name__ == "__main__":
    print_intro()
    while True:
        CHOICE = int(input("Would you like to: \n\
        1. Calculate simple and compound interest over time\n\
        2. Calculate the amount of time required to hit a savings goal.\n\
        3. Exit\n\
        : "))

        if CHOICE == 1:
            PRINCIPAL, RATE, YEARS = get_input()
            FINAL_SIMPLE_INTEREST = simple_interest(PRINCIPAL, RATE, YEARS)
            FINAL_COMPOUND_INTEREST = compound_interest(PRINCIPAL, RATE, YEARS)
            print_output_compounding(PRINCIPAL, RATE, YEARS, FINAL_SIMPLE_INTEREST)
            print_compounding_output(PRINCIPAL, RATE, YEARS, FINAL_COMPOUND_INTEREST)


        elif CHOICE == 2:
            PRINCIPAL_AMOUNT, INTEREST_RATE, SAVINGS_TARGET = get_target_input()
            EXPECTED_YEARS = calculate_years_to_target(PRINCIPAL_AMOUNT, INTEREST_RATE,\
             SAVINGS_TARGET)
            print_target_output(PRINCIPAL_AMOUNT, INTEREST_RATE, EXPECTED_YEARS)

        elif CHOICE == 3:
            print("Thank you for choosing us ...")
            break
        else:
            print("Invalid input ... please try again")
            break

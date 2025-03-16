#Simple interest calculator.
def housekeeping():
    principal = float(input("Enter the principle amount: "))
    rate = float(input("Enter the rate of interest (as a percentage):  "))
    time = float(input("Enter the time in years:  "))
    return principal, rate, time

def detailLoop(principal, rate, time):
    interest = principal * (rate/100)* time
    print(f"The simple interest is:  {interest:.2f}")
    
def finish():
    print("Thanks for calculating your interest!")
    
#Main program
principal, rate, time = housekeeping()
detailLoop(principal, rate, time)
finish()
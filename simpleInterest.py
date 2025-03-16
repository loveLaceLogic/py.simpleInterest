# Simple interest calculator

def get_user_input():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (as a percentage): "))
    time = float(input("Enter the time in years: "))
    return principal, rate, time

def calculate_simple_interest(principal, rate, time):
    interest = principal * (rate / 100) * time
    print(f"The simple interest is: {interest:.2f}")

def display_thank_you_message():
    print("Thank you for using the Simple Interest Calculator!")

# Main program
principal, rate, time = get_user_input()
calculate_simple_interest(principal, rate, time)
display_thank_you_message()

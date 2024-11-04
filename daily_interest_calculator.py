def calculate_daily_interest(principal, rate, days):
    # Calculate daily interest
    interest = principal * (rate / 100) * (days / 365)
    return interest

def main():
    print("Daily Interest Calculator")
    
    # Getting user input for principal, rate, and days
    try:
        principal = float(input("Enter the principal amount (in dollars): "))
        rate = float(input("Enter the annual interest rate (as a percentage): "))
        days = int(input("Enter the number of days: "))
        
        # Calculate the interest
        interest_amount = calculate_daily_interest(principal, rate, days)
        
        # Display the result
        print(f"\nThe calculated interest for ${principal:.2f} at {rate}% over {days} days is: ${interest_amount:.2f}")
        
    except ValueError:
        print("Please enter valid numeric values for principal, rate, and days.")

# Run the program
if __name__ == "__main__":
    main()

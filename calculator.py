# Loan Calculator

# Function to calculate monthly payment
def _mon_pay_(loan, interest, duration):

    # Interest rate
    r = ((interest / 100) / 12)

    # number of months
    mon = float(duration) * 12
    
    # Calculate and return the monthly payments
    if interest > 0:
        mon_pay = loan * r * ((1 + r) ** mon) / ((1 + r) ** mon - 1)
    else:
        mon_pay = loan /(duration * 12)
    # Return the value
    return round(mon_pay, 2)

# Calculating Remaining Balance
def _balance_(loan, interest, duration, paid):

    # Interest rate
    r = ((interest / 100) / 12)

    # number of months
    mon = float(duration) * 12
    
    # Calculate and return the monthly payments
    if interest > 0:
        bal = loan * (((1 + r) ** mon) - (1 + r) ** paid) / ((1 + r) ** mon - 1)
    else:
        bal = loan * (1 - (paid / mon))
    # Return the value
    return bal


# Main program starts
principal = float(input("Enter loan amount:"))
annual_interest_rate = float(input("Enter annual interest rate (percent):"))
duration = int(input("Enter loan duration in years:"))
month_pay = _mon_pay_(principal, annual_interest_rate, duration)

# Output Loan's Basic Details
print("LOAN AMOUNT:", principal ,"INTEREST RATE (PERCENT):", annual_interest_rate)
print("DURATION (YEARS):", duration ,"MONTHLY PAYMENT:", int(month_pay))

# Counting and Printing yearly payments and remaining balance
for y in range(1, duration + 1):
    month_pay = _mon_pay_(principal, annual_interest_rate, duration)
    paid = y * 12
    remain_bal = _balance_(principal, annual_interest_rate, duration, paid)
    print("YEAR:", y ,"BALANCE:", int(remain_bal) ,"TOTAL PAYMENT", int(month_pay * (y * 12)))

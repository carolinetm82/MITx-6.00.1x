"""

Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the credit
card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance.At the end of 12 months, print out the remaining balance.

"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


monthlyInterestRate = annualInterestRate/12


for n in range(12):
    # Compute the monthly payment, based on the previous month’s balance
    minimumMonthlyPayment = monthlyPaymentRate * balance
    
    # Update the outstanding balance by removing the payment
    monthlyUnpaidBalance = balance - minimumMonthlyPayment 
        
    #  then charging interest on the result
    UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    print('Month', n+1, 'Remaining balance:',round(UpdatedBalance,2))
    
    balance=UpdatedBalance
    
print('Remaining balance at the end of the year:',round(UpdatedBalance,2)) 

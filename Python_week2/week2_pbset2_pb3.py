'''
Problem 3 - Using Bisection Search to Make the Program Faster

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search to find the smallest monthly payment
to the cent (no more multiples of $10) such that we can pay off the debt within a year.

'''

balance = 999999
annualInterestRate = 0.18


balance_init=balance

monthlyInterestRate = annualInterestRate/12 


epsilon=0.01
lower_bound=balance/12
print('Initial lower_bound',round(lower_bound,2))
upper_bound=(balance * (1 + monthlyInterestRate)**12) / 12.0
print('Initial upper_bound',round(upper_bound,2))
minimumMonthlyPayment = (lower_bound + upper_bound) / 2
print('Initial minimumMonthlyPayment',round(minimumMonthlyPayment,2))


b=balance_init
 

while (b>0 and b<=epsilon)==False :
    b=balance_init
    
    for n in range(12):
       # Update the outstanding balance by removing the payment
       monthlyUnpaidBalance = b - minimumMonthlyPayment 
  
       # then charging interest on the result
       UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)

       b=UpdatedBalance
  
    
    if (b>0 and b<=epsilon)==True:
        break
    
    else:
        if b >= epsilon:
           lower_bound=minimumMonthlyPayment
        else:
           upper_bound=minimumMonthlyPayment
    
    minimumMonthlyPayment=(lower_bound + upper_bound) / 2
    
print('The smallest monthly payment such that we can pay off the debt within a year is',round(minimumMonthlyPayment,2),'$')  

balance = 3329
annualInterestRate = 0.2
balance_init=balance
monthlyInterestRate = annualInterestRate/12 

minimumMonthlyPayment = 0

while balance > 0 :

    b=balance_init
    
    for n in range(12):

    # Update the outstanding balance by removing the payment
        monthlyUnpaidBalance = b - minimumMonthlyPayment 
    
    #  then charging interest on the result
        UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    
        b=UpdatedBalance
    minimumMonthlyPayment += 10

    balance=UpdatedBalance
  
print(minimumMonthlyPayment-10)

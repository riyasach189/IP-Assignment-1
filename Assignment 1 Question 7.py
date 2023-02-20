#COMPLETED
#TESTED

"""
You have just entered college and would like to buy a laptop of cost, cost. 
Your monthly allowance is allowance, and you can save a fraction sf of it every month. 
Every month, you put your savings in a bank account that gives you a monthly rate of interest r 
(interest is compounded). 
If your allowance is Rs 20,000, 
your saving fraction sf is 0.1, 
and the rate of interest r is 0.5, 
determine after how many months you will be able to purchase the laptop
and the amount of savings that will remain after purchase. 
For laptop cost, take the input from the user (try Rs 65000, 45000, 125000, etc.)

Hint. Keep track of your total savings after every month - 
you have to add the interest you earn on your total savings of 
last month and the savings of this month. 
For (i) write a function that takes the cost and other parameters, 
and keeps increasing the month count from 1 onwards, 
till your savings become more than cost and returns the number 
of months and the remaining saving (recall that return can return more than one value). 
In the main program, you take the cost as input and then call this function. 

Bonus Problem. Suppose you want to buy the laptop in fewer months. 
As the interest rate is not in your control, you can only change the saving fraction. 
Determine the savings rate needed for different numbers of months for purchasing the laptop, 
starting from the number of months determined earlier. 
"""

cost = float(input("Enter cost: "))
ALLOWANCE = 20000
SF = 0.1
R = 0.5
savings = 0
months = 0

def bank_acc(savings,months,cost,SF=0.1,R=0.5,ALLOWANCE=20000):
    savings += ALLOWANCE*SF

    if savings<cost:
        savings += savings*R/100
    
    months += 1
    return(savings,months)

while(savings<cost):
    savings, months = bank_acc(savings, months,cost)

savings = savings - cost

print(f"No. of months: {months}")
print(f"Savings left: {savings}")
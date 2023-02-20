#COMPLETED; code is not optimal
#TESTED

"""
Two variable optimization.
Many problems require optimization of some function - minimizing (e.g., loss) or maximizing (e.g., profit) 
given some function and some constraints. This is an example of this problem.

A furniture company manufactures dining room tables and chairs. 
The relevant manufacturing data are given in the table.

Department              Labour Hours per table            Labour Hours per chair     Max Labour hours available per day
Assembly                        8                                   2                           400
Finishing                       2                                   1                           120
Profit per Unit         $90 for first M units               $25 for first M units 
                          $100 after that                     $30 after that

Write a program to determine how many tables and chairs should be manufactured each day
to realize a maximum profit. Print the number of chairs, tables, and the maximum profit. 
Initially have M = 10. Run the program again for M = 0, 20 and see how the output changes. 
Keep the code to compute this simple (even if it is inefficient), and you do not have to 
optimize the code.

Hint: Let x1 represent the number of tables and x2 represent the number of chairs. 
Determine the equations for total profit P, and the constraints on the two types of labor hours. 
Write functions to compute P and each constraint (these will be very simple functions). 
Have a statement in main program to set M and pass it to function for computing profit
- you can change the value of M for different runs of the program.
Write the main program that ranges over the values of x1 and x2
(from min possible value to max possible value) to find at which values max is reached.
"""

m = int(input("Enter M: "))
max_profit = 0
max_t = 60
max_c = 200
tables = 0
chairs = 0

def profit(t,c,m):
    profit = 0
    
    if m>t:
        profit += t*90
    else:
        profit += m*90 + (t-m)*100
    if m>c:
        profit += c*25
    else:
        profit += m*25 + (c-m)*30
         
    return(profit)

def assembly(t,c):
    if (8*t+2*c)<=400:
        return True
    else:
        return False

def finishing(t,c):
    if (2*t+c)<=120:
        return True
    else:
        return False

for t in range(max_t+1):
    for c in range(max_c+1):
        if assembly(t,c) and finishing(t,c):
            if profit(t,c,m)>max_profit:
                max_profit = profit(t,c,m)
                tables = t
                chairs = c

print (f"The maximum profit is: {max_profit}")
print (f"The no. of tables is: {tables}")
print (f"The no. of chairs is: {chairs}")


#maximum profit possible is 5200 at m=0
#minimum profit possible (by changing the value of m) is 4600 at m>=40
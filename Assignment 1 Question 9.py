#COMPLETED
#TESTED

"""
The demand for an item in the market (in terms of the number of items) decreases 
as the price (p) of the items increases. 
On the other hand, the supply of the item increases 
as the price increases (as producers expect to make more profit). 
Suppose the demand and supply changes as follows with price:
 
Demand function, D is:  ln D(p) = a - b*p  (i.e. D(p) is e to the power of rhs)
Supply function, S is: ln S(p) = c + d*p 

An equilibrium is achieved when demand and supply match (approximately) 
- this is a basic economics theory. Determine at what price an equilibrium will be reached, 
and output the equilibrium price and the number of items produced/bought at this equilibrium. 
Given a minimum price, find at what price an equilibrium is found, if it exists. 
(If no solution is possible - print that.) Iterate by starting with the minimum price 
and increasing the price by 5% every time (so your equilibrium will not be precise), 
to find the equilibrium. Your program should print the equilibrium price, 
and the demand and supply at that price. For this take a, b, c, d as 10, 1.05, 1, 1.06.  
You can assume that the minimum price as 1.0.

Hint: Write a function to compute demand and another to compute supply 
(for given coefficients and a given price). In main, you start with the initial price, 
call the function repeatedly with increased price to find where the demand and supply finally cross.
"""

count = 0

def demand(p):
    demand = 10 - (1.05*p)
    return(demand)

def supply(p):
    supply = 1 + (1.06*p)
    return(supply)

price = 1

min_diff = demand(price)-supply(price)

while (min_diff>0.000001):
    count+=1
    if (demand(price)-supply(price))<min_diff:
        min_diff = demand(price)-supply(price)
        
    price+=0.000001

    if count>=10000000:
        break

if count>=10000000:
    print("Equilibrium does not exist.")

else:
    D = 2.718**(demand(price))
    S = 2.718**(supply(price))

    print(f"Equilibrium price: {price}")
    print(f"Demand at equilibrium: {D}")
    print(f"Supply at equilibrium: {S}")

#program is a little slow because of the conditions on count, min_diff and price
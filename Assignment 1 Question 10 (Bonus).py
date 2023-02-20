#COMPLETED
#TESTED

"""
Write a program to computationally find a root of a given polynomial in x. 
Your program should have a function to compute the value of the polynomial for a given value of x 
(you can assign the coefficients in the first few statements and then compute and return the value). 
You should have another function that takes as parameters the function to 
compute the polynomial and an initial value of x (x0), which is used to find the root. 
For computing the root of the polynomial, use the newton-Raphson method (look it up) - 
it will start with assuming the initial root as x0, and if the value of the polynomial is not 0 at x0, 
determine the slope at x0 to find x1 - the point where the straight line with this slope will 
intersect the x-axis. Then use this x1 and repeat the process. 
Till the value of the polynomial reaches close to 0 
(you can assume that if the polynomial is within +/-0.2, it is a root).

Your main program should ask for the value of x0 and then compute the root. 
Try with different values of x0 and see what root it finds -
you will see that starting point can lead to different roots. 
As newton Raphson may not converge, or the polynomial may not have a root, 
after trying for some number iterations (say 100), your program should print a suitable message and quit.

For the problem, use the polynomial: x**3 - 10.5*x**2 + 34.5*x - 35  
(FYI, this one has 3 different roots)

Bonus problem: Given that the polynomial has n roots and a range x1 and x2 
within which all the roots are, expand the root finding program to find all the roots between x1 and x2.
"""

x1 = float(input("Starting point: "))
x2 = float(input("Ending point (inclusive): "))
roots = []

def f(x):
    f = x**3 - 10.5*x**2 + 34.5*x - 35
    return f

def f1(x):
    if x!=0:
        coefficients = [-35, 34.5, -10.5, 1]
        f1 = 0
        for i in range(len(coefficients)):
            f1 += i*coefficients[i]*x**(i-1)

        return f1

    else:
        return 0.01

for i in range(round(x1*10),round(x2*10)):
    x0 = i/10

    while (True):
        x = x0 - (f(x0)/f1(x0))
        
        if abs(x-x0)<0.00001:
            break
        
        x0 = x

    if round(x,1) not in roots:
        if x1<=x<=x2:
            roots.append(round(x,1))

if bool(roots)==0:
    print("No roots in the given range.")

else:  
    roots.sort()
    print(f"Root(s) of the polynomial in the given range is/are: {roots}")
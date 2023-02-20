#COMPLETED
#TESTED

"""
Write a function that takes a positive integer “n” as a parameter 
and prints the pattern of the type given below for n=7. 

*            *
**          **
***        ***
****      ****
*****    *****
******  ******
**************

Remember that print("*", end="") will not print the newline, 
and you can print() and can just print a new line. 
In the main program, take user input as n and call this function for printing.
"""

n = int(input("Enter a positive integer: "))

def triangles(n):
    for i in range(1,n+1):
        print("*"*i + " "*(2*(n-i)) + "*"*i)
    return()

if n<0:
    print("Invalid input")
else:
    triangles(n)
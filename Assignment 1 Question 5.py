#COMPLETED
#TESTED

"""
A person is standing and is looking at a pole in front of him.
Given the angle of view to the top (in degrees - should be between 0 and 90)
and the horizontal distance from the person to the base of the pole (in meters), 
you have to find the height of the pole and the length of the line from the person to the top of the pole.
 
Your program has to take as input (from the user on the terminal) the angle (in degrees) 
and another input for distance to the base of the pole. 
Then it computes and prints the height of the pole and the distance to the tip of the pole.
 
Note. You must write functions to compute sin(), cos(), … using the series for them 
and cannot use the python provided functions (e.g., in the math module). 
If the value of pi is needed, you can use the standard value (3.14). 
First, write these functions and test them. 
Then write the main program to take inputs for angle and distance, 
and call the functions to compute the height and distance.
"""

PI = 3.14
angle = int(input("Enter an angle between 0 and 90 degrees: "))
distance = float(input("Enter the horizontal distance from the person to the base of the pole (in meters): "))
angle = PI*angle/180
pole_height = 0
distance_to_tip = 0

def factorial(a):
    fact = 1
    while a>1:
        fact = fact*a
        a = a-1
    return fact

def sin(a):
    n = 1
    sinx = 0
    for i in range(10):
        sinx = sinx + ((-1)**i)*((a**n)/factorial(n))
        n = n+2
    return sinx

def cos(a):
    n = 0
    cosx = 0
    for i in range(10):
        cosx = cosx + ((-1)**(i))*((a**n)/factorial(n))
        n = n+2
    return cosx

def tan(a):
    tanx = sin(a)/cos(a)
    return tanx

pole_height = distance*tan(angle)
distance_to_tip = distance/cos(angle)

print(f"The height of the pole is: {pole_height}")
print(f"The distance of the person from the tip of the pole is: {distance_to_tip}")


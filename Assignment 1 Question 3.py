#COMPLETED
#TESTED

"""
Distance traveled. A vehicle is to travel on demand. 
Its initial location is given as x0, y0 (assume the first statement in your program as 
assigning initial values, say x0,y0 = 5.0, 5.0).
Repeatedly take as input the distance the vehicle has to travel.
If the input given is 0 or lesser, the travel ends - assume that at least one positive distance will be given.
The direction in which the vehicle is to travel is determined as follows: 
if distance is <= 25 it travels north, 
if between 26-50 it travels south, 
between 51 and 75 it travels east, 
and >= 76 it travels west.
Find the final coordinate of the vehicle, the total distance it has traveled, 
and the straight line distance between the initial location and the final location
(use standard formula for distance between two coordinates; 
note that this distance is not same as total distance traveled).

Hint: Initialize current coordinates x,y to x0,y0, and distance traveled to 0. 
For taking the distance use a while loop (as you dont know how many distances will be given). 
This can be done in two ways - you can initialize a variable (say dist) to some +ve value, and then loop till the value is 0 (or lesser) and in the loop get the input from the user for next distance.
Alternatively, you can have an infinite while loop, and take input in the loop and break if the input given is 0 (or lesser).
For each input distance, determine the new coordinates, and keep track of total distance traveled.
After the loop is done, compute the distance also.
"""

distance = 0
displacement = 0
x0 = float(input("Enter initial x-coordinate: "))
y0 = float(input("Enter initial y-coordinate: "))
x_final = x0
y_final = y0

while(True):
    num = float(input("Enter the distance: "))
    if num>0:
        distance += num
        
        if num<=25:                     # if distance is <= 25 it travels north
            y_final += num
        elif 25<num<=50:               # if between 26-50 it travels south
            y_final -= num
        elif 50<num<=75:               # between 51 and 75 it travels east
            x_final += num
        elif num>75:                   # and >= 76 it travels west
            x_final -= num
    else:
        break
    

displacement = ((x_final-x0)**2 + (y_final - y0)**2)**(1/2)
print(f"The final coordinates are: ({x_final}, {y_final})")
print(f"The final distance is: {distance}")
print(f"The final displacement is: {displacement}")
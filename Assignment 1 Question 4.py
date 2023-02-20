#COMPLETED
#TESTED

"""
Integration through computation. Suppose the velocity of a rocket at a time t is given by: 
f(t) = 2000ln[140000/(140000 - 2100t)] - 9.8t
Take as input starting time (a) and ending time (b),
and find the distance covered by a rocket between time a and b. 
For computationally determining the distance, work with time increments (delta) of 0.25 seconds. 
You can use the math module of python for this problem.

Hint: Compute the velocity at time t and t+delta, take the average, 
and then compute the distance traveled in this delta time duration. 
Start from a and keep computing in increments of delta till b.
"""

import math

a = int(input("Enter the start time in seconds: "))
b = int(input("Enter the end time in seconds: "))
distance = 0
velocity = 0
velocity_next = 0

for t in range((a*1000),(b*1000)):
    velocity = 2000*(math.log(140000/(140000 - 2100*(t/1000)))) - 9.8*(t/1000)
    velocity_next = 2000*(math.log(140000/(140000 - 2100*((t+1)/1000)))) - 9.8*((t+1)/1000)
    distance += ((velocity+velocity_next)/2)*0.001

print(f"Distance covered by rocket (in meters): {distance}")
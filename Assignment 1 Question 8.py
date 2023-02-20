#COMPLETED
#TESTED

"""
The current population of the world is combined together into groups that are growing at different rates, 
and the population of these groups is given (in millions) in a list.  
The population of the first group (is Africa) is currently growing at 2.5% per year, 
and each subsequent group is growing at 0.4% lesser i.e. the next group is growing at 2.1%
(note: the growth rate can be negative also). 
For each group, every year, the growth rate reduces by 0.1. 
With this, eventually, the population of the world will peak out and after that start declining. 
Write a program that prints: 
(i) the current total population of the world, 
(ii) the years after which the maximum population will be reached, 
(iii) and the value of the maximum population.

Hint: Write a function to compute the population of a group after n years, 
given the initial population and the current rate of growth. 
For this, you compute the population after every year till n 
(note that the growth rate for each year can be determined easily once the initial rate is known). 
In the main program, you can loop increasing the years (Y) from 1 onwards, 
and for each Y, you will need to compute the value of each group after Y years using
the function and compute the total population of the world as a sum of these. 
To check if the population is declining, save the population for the previous Y, 
and every year check if the population has declined - if it has declined, 
the previous year's population was the highest (otherwise, 
this year's population will become the previous year's for next iteration).

The first statement in your program should give the population as an assignment:
pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
In the program, you can loop over this list, but you cannot use any list functions
(and you need not index into the list).
"""

population = [50, 1450, 1400, 1700, 1500, 600, 1200]
growth_rate = [2.5, 2.1, 1.7, 1.3, 0.9, 0.5, 0.1]
sum = 0
max = 0
max_pop = []
n = 0

current_year = int(input("Enter years after which population is to be determined: "))

def pop_after_n_years(pop,gr,n=1):

    for i in range(n):
        for i in range(7):
            pop[i] += pop[i]*gr[i]/100

        for i in range(7):
            gr[i] = gr[i]-0.1

    return(pop)

new_pop = pop_after_n_years(population, growth_rate, current_year)

for i in new_pop:
    sum += i

print(f"Current population: {sum}")

population = [50, 1450, 1400, 1700, 1500, 600, 1200]
growth_rate = [2.5, 2.1, 1.7, 1.3, 0.9, 0.5, 0.1]
sum = 0

while(max<=sum):
    max = sum
    sum = 0
    max_pop = pop_after_n_years(population, growth_rate)

    for i in max_pop:
        sum += i

    n += 1
    
print(f"Maximum population: {max}")
print(f"Years after which maximum population is reached: {n-1}")

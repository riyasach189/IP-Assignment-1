#COMPLETED
#TESTED

"""
This program uses a pseudo random number generator to make three different games:
1 - Rock, Paper, Scissors
2 - Lucky Dice Roll
3 - Totally True Future Predictor

prng formula source: https://www.freecodecamp.org/news/random-number-generator/
"""

num = int(input("Enter 1 for Rock, Paper, Scissors; 2 for Lucky Dice Roll; 3 for Totally True Future Predictor: "))

def random(x):                              
    m = 121
    a = 29
    b = 61
    for i in range(x):
        random = (x*a + b)%m
        x = random
   
    return(random)

if num==1:
    #Sometimes, it gets stuck on one output. Not able to correct that.

    random_num = int(input("Enter any natural number you want to. (Greater than 0): "))
    x = random(random_num)
    
    while(True):
        print("")
        user_move = int(input("Enter 0 for Rock; 1 for Paper; 2 for Scissors; anything else to exit the game: "))
        my_move = x%3
        
        if user_move<0 or user_move>2:
            print("Incorrect input. I'm not playing with you.")
            break

        if my_move==0:
            print("My move: Rock")
            
        elif my_move==1:
            print("My move: Paper")
            
        elif my_move==2:
            print("My move: Scissors")

        if user_move==my_move:
            print("It's a tie.")
        elif user_move-my_move==1 or user_move-my_move==-2:
            print("Darn it. You won.")
        else:
            print("Ha! I won.")

        x = random(x)+(my_move*5)
            
elif num==2:
    flag = "y"

    while(flag=="y"):
        random_num = int(input("Enter any natural number you want to. (Greater than 0): "))
        x = random(random_num) 
        print("")
        n1 = (x%6)+1
        print(f"Your first number is: {n1}")

        random_num = int(input("Enter another natural number. (Greater than 0): "))
        x = random(random_num) + random_num
        print("")
        n2 = (x%6)+1
        print(f"Your second number is: {n2}")

        if n1+n2==7:
            print("Your numbers add up to 7. You won.")
        else:
            print("Your numbers don't add up to 7. You lost.")        #Winning combination: (1,2),(7,10)

        flag = input("Enter y to play again: ")

elif num==3:
    flag = "y"
    while(flag=="y"):
        random_num = int(input("Enter any natural number you want to. (Greater than 0): "))
        x = random(random_num)

        que = input("Enter a \"yes/no\" question: ")
        if x%3==0:
            print("Yes")
        elif x%3==1:
            print("No")
        else:
            print("Maybe")
        
        flag = input("Enter y to play again: ")

else: 
    print("Looks like you don't want to play.")
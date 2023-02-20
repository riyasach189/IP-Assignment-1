#COMPLETED
#TESTED

"""
Write a program to take as input a number between 0 and 99, and print the text equivalent of the number.
I.e., for inputs 5, 13, 43, and 85, outputs are "five", "thirteen", "forty three", and "eighty five".
(Hint: Have a function to write the text for tens digit, and another to write the text for the unit digit - use of elif construct will be helpful in these.
In main, take the input, get the decimal and units digits of the number and print their text.
The code is simple though it may be long as you have to print for different cases. 
You may first write a function to print the text for a units digit and test it, and then build the rest)

Bonus Question. Expand the code above to write in text any number lesser than 100 crore. 
(FYI we have: units, tens, hundred, thousand, ten-thousand, lac, ten-lac, crore, ten-crore).
"""

n = int(input("Enter a number less than 100: "))
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
numtotext = ""

if n>=100:
    print("Input is too large.")

elif n==0:
    print("zero")

else:
    b = n//10
    a = n%10
    if b==0:
        numtotext = ones[a]

    elif b!=1:
        numtotext = tens[b]+" "+ones[a]

    else:
        numtotext = teens[a]

    print(f"The text equivalent is: {numtotext}")

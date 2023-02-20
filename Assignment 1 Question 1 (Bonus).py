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

n = int(input("Enter a number less than 100 crore: "))
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
numtotext = ""

if n>=1000000000:
    print("Input is too large.")

elif n==0:
    print("zero")

#the code is neither optimal nor organised, but it works. Any other variation I tried had bugs.

else:
    a = n//100000000
    n = n%100000000
    b = n//10000000
    n = n%10000000
    c = n//1000000
    n = n%1000000
    d = n//100000
    n = n%100000
    e = n//10000
    n = n%10000
    f = n//1000
    n = n%1000
    g = n//100
    n = n%100
    h = n//10
    i = n%10
    
    if a==1:
        numtotext += teens[b]+ " crore "
    elif a!=0 and b!=0:
        numtotext += tens[a]+" "+ones[b]+ " crore "
    elif a!=0 and b==0:
        numtotext += tens[a]+" crore "
    elif a==0 and b!=0:
        numtotext += ones[b]+ " crore "

    if c==1:
        numtotext += teens[d]+ " lakh "
    elif c!=0 and d!=0:
        numtotext += tens[c]+" "+ones[d]+ " lakh "
    elif c!=0 and d==0:
        numtotext += tens[c]+" lakh "
    elif c==0 and d!=0:
        numtotext += ones[d]+ " lakh "
    
    if e==1:
        numtotext += teens[f]+ " thousand "
    elif e!=0 and f!=0:
        numtotext += tens[e]+" "+ones[f]+ " thousand "
    elif e!=0 and f==0:
        numtotext += tens[e]+" thousand "
    elif e==0 and f!=0:
        numtotext += ones[f]+ " thousand "

    if g!=0:
        numtotext += ones[g]+ " hundred "

    if h==1:
        numtotext += teens[i]
    elif h!=0 and i!=0:
        numtotext += tens[h]+" "+ones[i]
    elif h!=0 and i==0:
        numtotext += tens[h]
    elif h==0 and i!=0:
        numtotext += ones[i]


    
    print(f"The text equivalent is: {numtotext}")
# Instructions
'''
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
'''

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total += total * int(tip)/100

#pay = round(total/int(people),2)

pay = "{:.2f}".format(total/int(people))

print(f"Each person should pay: {pay}")

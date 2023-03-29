names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

pay = names[random.randint(0, len(names) - 1)]

print(pay + " is going to buy the meal today")

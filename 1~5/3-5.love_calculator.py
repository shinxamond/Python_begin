print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = (name1 + name2).lower()

name_count1 = 0
name_count2 = 0

name_count1 += name.count("t")
name_count1 += name.count("r")
name_count1 += name.count("u")
name_count1 += name.count("e")

name_count2 += name.count("l")
name_count2 += name.count("o")
name_count2 += name.count("v")
name_count2 += name.count("e")

#name_count = int(str(name_count1)+str(name_count2))
name_count = name_count1 * 10 + name_count2
print(type(name_count))

if (name_count<10) or (name_count>90) :
  print(f"Your score is {name_count}, you go together like coke and mentos.")
elif (40<=name_count) and (name_count<=50) :
  print(f"Your score is {name_count}, you are alright together.")
else :
  print(f"Your score is {name_count}.")
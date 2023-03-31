fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)  #들여쓰기

#For Loop with Range
for number in range(1, 10, 3):
  #not include 10
  # 3씩 증가
  print(number)

#1부터 100까지 더하기
total = 0
for hundred in range(1, 101):
  total += hundred
print(total)
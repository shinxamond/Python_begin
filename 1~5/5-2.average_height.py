# don't use : sum(), len()

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height_sum = 0
people = 0

for i in student_heights:
  height_sum += i
  people += 1
  
print(round((height_sum) / people))
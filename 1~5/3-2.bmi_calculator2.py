'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# A**B : A의 B제곱
result = weight/height**2

#What I want : 18.6처럼 소수점 첫째 자리에서 끝나도 18.60처럼 둘째 자리까지 0으로 채워서 출력. 단, 코드가 가장 짧게

#1. format 메서드를 이용하면 str이 된다.
#bmi = "{:.2f}".format(result)

#2. '%.?f'는 print() 사용 시에만 가능
#bmi = ('%.2f',%result)

#3. round()는 18.6으로 짤린다.
#bmi = round(result,2)

#4. f-string 방식 (채택)
print(f"Your bmi is {result:.2f}.")

if result < 18.5 :
  print("You are underweight.")
elif result < 25 :
  print("You are normal weight.")
elif result < 30 :
  print("You are overweight.")
elif result < 35 :
  print("You are obese.")
else :
  print("You are clinically obese.")
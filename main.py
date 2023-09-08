#Data Types
# 🚨 Don't change the code below 👇
print("Welcome to Body Mass Index (BMI) Calculator")
print("Know if you are Overweight, Normal or Underweight")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

def user_bmi(bmi):
  underweight = range(0, 20)
  normal = range(19, 26)
  overweight = range(25, 31)
  if bmi in underweight:
    print('You are underweight')
  elif bmi in normal:
    print('Your weight is normal')
  elif bmi in overweight:
    print('You are overweight')
  elif bmi > 30:
    print('You are obese')
  else:
    print("We can't provide something, check back")
#Write your code below this line 👇
integer_weight = int(weight)
integer_height = float(height)
# print(type(integer_height), type(integer_weight))
bmi = integer_weight / (integer_height * integer_height)
integer_bmi = int(bmi)
print("Your BMI is ",integer_bmi)
user_bmi(integer_bmi)

 
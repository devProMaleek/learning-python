# Data Types
# 🚨 Don't change the code below 👇
print("Welcome to Body Mass Index (BMI) Calculator")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆


def user_bmi(bmi):
    underweight = range(0, 20)
    normal = range(19, 26)
    overweight = range(25, 31)
    if bmi in underweight:
        print(f"Your BMI is {bmi}, you are underweight")
    elif bmi in normal:
        print(f"Your BMI is {bmi}, you have a normal weight")
    elif bmi in overweight:
        print(f"Your BMI is {bmi}, you are slightly overweight")
    elif bmi > 30:
        print(f"Your BMI is {bmi}, you are obese")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese")


# Write your code below this line 👇
integer_weight = float(weight)
integer_height = float(height)
# print(type(integer_height), type(integer_weight))
bmi = integer_weight / (integer_height * integer_height)
integer_bmi = float(bmi)
# print("Your BMI is ", integer_bmi)
user_bmi(round(integer_bmi))


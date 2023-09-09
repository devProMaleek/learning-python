# #Data Types
# # 🚨 Don't change the code below 👇
# print("Welcome to Body Mass Index (BMI) Calculator")
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# def user_bmi(bmi):
#   underweight = range(0, 20)
#   normal = range(19, 26)
#   overweight = range(25, 31)
#   if bmi in underweight:
#     print('You are underweight')
#   elif bmi in normal:
#     print('Your weight is normal')
#   elif bmi in overweight:
#     print('You are overweight')
#   elif bmi > 30:
#     print('You are obese')
#   else:
#     print("We can't provide something, check back")
# #Write your code below this line 👇
# integer_weight = int(weight)
# integer_height = float(height)
# # print(type(integer_height), type(integer_weight))
# bmi = integer_weight / (integer_height * integer_height)
# integer_bmi = int(bmi)
# print("Your BMI is ",integer_bmi)
# user_bmi(integer_bmi)


# F-String
# Manipulating different data types together
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Life in Weeks Challenge

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
actual90Days = 90 * 365
actual90Weeks = 90 * 52
actual90Months = 90 * 12

ageAsInt = int(age)

userDaysSpent = ageAsInt * 365
userWeeksSpent = ageAsInt * 52
userMonthsSpent = ageAsInt * 12

userDaysLeft = actual90Days - userDaysSpent
userWeeksLeft = actual90Weeks - userWeeksSpent
userMonthsLeft = actual90Months - userMonthsSpent

result = f"You have {userDaysLeft} days, {userWeeksLeft} weeks, and {userMonthsLeft} months left"

print(result)

 
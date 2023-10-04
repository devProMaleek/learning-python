# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_length = len(names)
random_person = names[random.randint(0, names_length - 1)]
print(f"{random_person} is going to buy the meal today!")

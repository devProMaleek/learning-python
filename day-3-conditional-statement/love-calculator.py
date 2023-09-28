# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


# Write your code below this line 👇
def true_count(name):
    true_count = 0
    true_count += name.count("t")
    true_count += name.count("r")
    true_count += name.count("u")
    true_count += name.count("e")
    return true_count


def love_count(name):
    love_count = 0
    love_count += name.count("l")
    love_count += name.count("o")
    love_count += name.count("v")
    love_count += name.count("e")
    return love_count


combined_names = name1 + name2

true_count = true_count(combined_names.lower())
love_count = love_count(combined_names.lower())
love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

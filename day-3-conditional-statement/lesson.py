print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
    # Nested if-else
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5, and enjoy your ride.")
    elif age > 12 and age < 19:
        print("Please pay $7, and enjoy your ride.")
    else:
        print("Please pay $12, and enjoy your ride.")
else:
    print("Sorry, you have to grow taler before your ride")

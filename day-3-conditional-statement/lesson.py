print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    # Nested if-else
    age = int(input("What is your age? "))
    if age <= 12:
        total_bill += 5
        print("Child tickets are $5.")
    elif age > 12 and age < 19:
        total_bill += 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        total_bill += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ").lower()
    if wants_photo == "y":
        total_bill += 3
        print(f"Your total bill is ${total_bill}. Thank you and enjoy the ride!")
else:
    print("Sorry, you have to grow taller before you can ride")

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computer_choice = random.randint(0, 2)


def print_choice(choice):
    if choice == 0:
        print(f"You chose Rock:\n{rock}")
    elif choice == 1:
        print(f"You chose Paper:\n{paper}")
    elif choice == 2:
        print(f"You chose Scissors:\n{scissors}")
    else:
        print("Invalid choice.")
        return


def print_computer_choice(choice):
    if choice == 0:
        print(f"Computer chose Rock:\n{rock}")
    elif choice == 1:
        print(f"Computer chose Paper:\n{paper}")
    elif choice == 2:
        print(f"Computer chose Scissors:\n{scissors}")
    else:
        print("Invalid choice.")
        return


def print_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif user_choice == 1 and computer_choice == 0:
        print("You win.")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win.")
    else:
        print("Invalid choice.")
        return


if user_choice >= 0 and user_choice <= 2:
    print_choice(user_choice)
    print_computer_choice(computer_choice)
    print_result(user_choice, computer_choice)
else:
    print("Invalid choice.")

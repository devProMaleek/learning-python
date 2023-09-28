print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right"'
)

if direction.lower() == "right":
    print("You fell into a hole. Game over.")
elif direction.lower() == "left":
    action = input(
        'There is a lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    )
    if action.lower() == "swim":
        print("You got attacked by an angry trout. Game over.")
    elif action.lower() == "wait":
        door = input(
            "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
        )
        if door.lower() == "red":
            print("It's a room full of fire. Game over.")
        elif door.lower() == "yellow":
            print("You found the treasure! You win!")
        elif door.lower() == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")

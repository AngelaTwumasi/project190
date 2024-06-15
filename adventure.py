def intro():
    print("You find yourself in a dark forest with two paths.")
    print("Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def left_path():
    print("You walk down the left path and encounter a river.")
    print("Do you want to swim across or walk along the river?")
    choice = input("Type 'swim' or 'walk': ").lower()
    if choice == "swim":
        swim_river()
    elif choice == "walk":
        walk_river()
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("You walk down the right path and find a treasure chest.")
    print("Do you want to open the chest or leave it?")
    choice = input("Type 'open' or 'leave': ").lower()
    if choice == "open":
        open_chest()
    elif choice == "leave":
        leave_chest()
    else:
        print("Invalid choice. Try again.")
        right_path()

def swim_river():
    print("You swim across the river and find a hidden cave.")
    print("Inside the cave, you find a sleeping dragon.")
    print("Do you want to sneak past the dragon or go back?")
    choice = input("Type 'sneak' or 'back': ").lower()
    if choice == "sneak":
        sneak_past_dragon()
    elif choice == "back":
        left_path()
    else:
        print("Invalid choice. Try again.")
        swim_river()

def walk_river():
    print("You walk along the river and find a small village.")
    print("The villagers welcome you and offer you food and shelter.")
    print("You have successfully completed your adventure. Congratulations!")
    play_again()

def open_chest():
    print("You open the chest and find a pile of gold coins.")
    print("Congratulations! You are rich!")
    play_again()

def leave_chest():
    print("You leave the chest and continue walking.")
    print("After a while, you find a peaceful meadow and decide to rest.")
    print("You have successfully completed your adventure. Congratulations!")
    play_again()

def sneak_past_dragon():
    print("You try to sneak past the dragon, but it wakes up!")
    print("The dragon is angry and breathes fire at you.")
    print("You have been burned to ashes. Game over.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Thank you for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        play_again()

# Start the game
intro()

def start_game():
    print("You find yourself in a dark forest. There are two paths in front of you.")
    print("1. Take the left path")
    print("2. Take the right path")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice! Please try again.")
        start_game()

def left_path():
    print("You walk along the left path and find a treasure chest.")
    print("1. Open the chest")
    print("2. Ignore the chest and keep walking")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("You open the chest and find gold coins! You win!")
    elif choice == '2':
        print("You ignore the chest and keep walking. Unfortunately, you get lost. Game over.")
    else:
        print("Invalid choice! Please try again.")
        left_path()

def right_path():
    print("You walk along the right path and encounter a wild animal.")
    print("1. Fight the animal")
    print("2. Run away")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("You fight bravely and defeat the animal! You win!")
    elif choice == '2':
        print("You run away safely, but get lost in the forest. Game over.")
    else:
        print("Invalid choice! Please try again.")
        right_path()

start_game()
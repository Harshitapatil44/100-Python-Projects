def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a dark forest.")

    while True:
        choice = input("Go left or right? ").lower()
        if choice == "left":
            river()
            break
        elif choice == "right":
            cave()
            break
        else:
            print("Invalid choice. Try again.")


def river():
    print("\nYou reached a river.")
    choice = input("Swim or build boat? ").lower()

    if choice == "swim":
        print("A crocodile attacked you.")
        print("Game Over.")
    elif choice == "build boat":
        print("You crossed safely.")
        treasure()
    else:
        print("Wrong choice.")
        river()


def cave():
    print("\nYou entered a cave.")
    choice = input("Light torch or walk in dark? ").lower()

    if choice == "light torch":
        print("You found hidden gold.")
        treasure()
    elif choice == "walk in dark":
        print("You fell into a pit.")
        print("Game Over.")
    else:
        print("Wrong choice.")
        cave()


def treasure():
    print("\nYou found the treasure chest!")
    choice = input("Open it? yes/no ").lower()

    if choice == "yes":
        print("Congratulations! You won the game.")
    else:
        print("You left the treasure and escaped safely.")
start_game()


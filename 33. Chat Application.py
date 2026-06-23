messages = []

while True:
    print("\n--- Chat Application ---")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        msg = input("Enter message: ")
        messages.append(msg)
        print("Message sent!")
    elif choice == "2":
        print("\nChat History:")
        if len(messages) == 0:
            print("No messages yet.")
        else:
            for i, msg in enumerate(messages, start=1):
                print(f"{i}. {msg}")
    elif choice == "3":
        print("Exiting chat...")
        break
    else:
        print("Invalid choice! Try again.")

class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, content):
        self.text += content

    def show(self):
        print("\nCurrent Text:")
        print(self.text)

    def clear(self):
        self.text = ""
        print("Text Cleared")


editor = TextEditor()

while True:
    print("\n1. Write Text")
    print("2. Show Text")
    print("3. Clear Text")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        content = input("Enter text: ")
        editor.write(content + "\n")

    elif choice == "2":
        editor.show()

    elif choice == "3":
        editor.clear()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

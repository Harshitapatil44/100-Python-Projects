class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self):
        note = input("Enter note: ")
        self.notes.append(note)
        print("Note added successfully!")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("\nYour Notes:")
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")

    def delete_note(self):
        self.view_notes()
        if self.notes:
            num = int(input("Enter note number to delete: "))
            if 1 <= num <= len(self.notes):
                self.notes.pop(num - 1)
                print("Note deleted successfully!")
            else:
                print("Invalid note number!")

app = NoteApp()

while True:
    print("\n--- Note Taking App ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.add_note()
    elif choice == "2":
        app.view_notes()
    elif choice == "3":
        app.delete_note()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")



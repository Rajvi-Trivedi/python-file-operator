import os 
from datetime import datetime

class Journal:
    def __init__(self, file="journal.txt"):
        self.file = file

    def add(self, text):
        try:
            with open(self.file, "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{text}\n\n")
            print("\nEntry added successfully!\n")
        except Exception as e:
            print("Error adding entry:", e)

    def view(self):
        try:
            with open(self.file, "r") as f:
                data = f.read()
                if data.strip():
                    print("\nYour Journal Entries:\n", data)
                else:
                    print("\nNo entries found.")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")
        print("Finished viewing entries.\n")

    def search(self, word):
        try:
            with open(self.file, "r") as f:
                data = f.read()
                entries = data.strip().split("\n\n")
                found = False
                for entry in entries:
                    if word.lower() in entry.lower():
                        print("\nMatching Entry:\n", entry.strip(), "\n")
                        found = True
                if not found:
                    print(f"\nNo entries found for: {word}")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")
        print("Search complete.\n")

    def delete(self):
        if os.path.exists(self.file):
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                os.remove(self.file)
                print("\nAll entries deleted successfully!\n")
                print("Delete operation complete.\n")
            else:
                print("\nDeletion cancelled.\n")
        else:
            print("\nNo journal entries to delete.\n")


print("Welcome to Personal Journal Manager!")
print("You can add, view, search, or delete your journal entries.\n")

j = Journal()

while True:
    
    print("\nMain Menu")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        text = input("\nEnter your journal entry: ")
        j.add(text)
    elif choice == "2":
        j.view()
    elif choice == "3":
        word = input("\nEnter a keyword or date to search: ")
        j.search(word)
    elif choice == "4":
        j.delete()
    elif choice == "5":
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("\nInvalid option. Please select a valid option from the menu.\n")

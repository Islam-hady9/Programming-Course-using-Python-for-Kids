def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print(f"Contact {name} added.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found!")

def contact_book():
    contacts = {}
    while True:
        print("\n1. View contacts\n2. Add contact\n3. Delete contact\n4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

contact_book()
import json

FILE = "contacts.json"


def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


def search_contact(contacts):
    name = input("Enter name to search: ")
    print(contacts.get(name, "Contact not found"))


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted.")
    else:
        print("Contact not found")


def main():
    contacts = load_contacts()

    while True:
        print("\n1. View  2. Add  3. Search  4. Delete  5. Exit")
        choice = input("Choose: ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice")


main()

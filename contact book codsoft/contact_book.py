import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully.\n")

# View all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} | 📞 {c['phone']} | 📧 {c['email']}")
    print()

# Search contact by name
def search_contact():
    keyword = input("Enter name to search: ").lower()
    found = [c for c in contacts if keyword in c['name'].lower()]
    if not found:
        print("❌ No matching contacts found.\n")
    else:
        for c in found:
            print(f"{c['name']} | 📞 {c['phone']} | 📧 {c['email']}")
        print()

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave field blank to keep current value.")
            new_name = input(f"New name ({c['name']}): ") or c['name']
            new_phone = input(f"New phone ({c['phone']}): ") or c['phone']
            new_email = input(f"New email ({c['email']}): ") or c['email']
            c['name'], c['phone'], c['email'] = new_name, new_phone, new_email
            save_contacts(contacts)
            print("✅ Contact updated.\n")
            return
    print("❌ Contact not found.\n")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    global contacts
    new_contacts = [c for c in contacts if c['name'].lower() != name]
    if len(new_contacts) != len(contacts):
        contacts = new_contacts
        save_contacts(contacts)
        print("🗑️ Contact deleted.\n")
    else:
        print("❌ Contact not found.\n")

# Main loop
def menu():
    while True:
        print("=== 📒 Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.\n")

# Run the program
contacts = load_contacts()
menu()

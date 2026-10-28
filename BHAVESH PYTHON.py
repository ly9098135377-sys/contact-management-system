# Contacts ko store karne ke liye ek global list jisme dictionaries hongi
contacts = []

def add_contact():
    """Naya contact add karne aur validate karne ka function"""
    name = input("Enter name: ")
    phone = input("Enter phone number (10 digits): ")
    
    # Phone number validation: exactly 10 digits hone chahiye
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Enter exactly 10 digits.")
        return
        
    # Duplicate check: phone number unique hona chahiye
    for c in contacts:
        if c['phone'] == phone:
            print("Contact with this number already exists.")
            return
            
    email = input("Enter email: ")
    # Dictionary me data store kiya ja raha hai
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print(f"Contact added: {name} | {phone}")

def read_contacts():
    """Sabhi contacts ko read/view karne ka function"""
    if not contacts:
        print("No contacts found.")
        return
    for c in contacts:
        print(f"{c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    """Naam ke dwara contact search karne ka function"""
    query = input("Enter name to search: ")
    found = False
    for c in contacts:
        if query.lower() in c['name'].lower():
            print(f"{c['name']} | {c['phone']} | {c['email']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    """Existing contact ka phone number update karne ka function"""
    name = input("Enter name of contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            new_phone = input("Enter new phone number: ")
            if not new_phone.isdigit() or len(new_phone) != 10:
                print("Invalid phone number. Enter exactly 10 digits.")
                return
            # Check duplicate for updated phone
            for other in contacts:
                if other['phone'] == new_phone and other != c:
                    print("Contact with this number already exists.")
                    return
            c['phone'] = new_phone
            print(f"Phone updated: {new_phone}")
            return
    print("Contact not found.")

def delete_contact():
    """Contact ko delete karne aur remaining contacts count dikhane ka function[cite: 1]"""
    name = input("Enter name to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print(f"Contact '{c['name']}' deleted. Total contacts: {len(contacts)}")
            return
    print("Contact not found.")

def main():
    """Loop-driven menu jisme exit option bhi shamil hai[cite: 1]"""
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
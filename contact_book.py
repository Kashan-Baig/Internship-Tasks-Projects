import json
import os
import re  # Import the regular expression module

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file) 
    return []  

def is_valid_email(email):
    # Basic email validation regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

while True:
    print("\n=== 📞 Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")
    contacts = load_contacts()

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        name = input("Enter name of contact: ")
        num = input("Enter contact number (11 Digits): ")
        email = input("Enter a valid email: ")
        
        # Validate both phone number and email
        if len(num) != 11:
            print("Number should be of 11 digits!")
            continue
            
        if not is_valid_email(email):
            print("Invalid email address format!")
            continue
            
        newcontact = {
            "name": name,
            "Contact Number": num,
            "Email Address": email 
        }
        contacts.append(newcontact)
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
        print("✅ Contact added successfully!")
        
    elif choice == 2:
        if not contacts:
            print("No contacts found.")
        else:
            print("\nALL Contacts:")
            for count, con in enumerate(contacts, 1):
                print(f"ID: {count}")
                print(f"Name: {con['name']}")
                print(f"Contact Number: {con['Contact Number']}")
                print(f"Email Address: {con['Email Address']}\n")
                
    elif choice == 3:
        search_term = input("Enter contact number or name to search: ")
        found = False
        for con in contacts:
            if (search_term.lower() in con["name"].lower() or 
                search_term == con["Contact Number"]):
                print("\nContact Found:")
                print(f"Name: {con['name']}")
                print(f"Contact Number: {con['Contact Number']}")
                print(f"Email Address: {con['Email Address']}")
                found = True
                break
        if not found:
            print("❌ Contact not found.")
               
    elif choice == 4:
        print("Thank you for using the contact book!")
        break
        
    else:
        print("Invalid choice! Please select 1-4.")
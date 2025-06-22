import json
import os
import re


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file) 
    return []  


while True:
    print("\n=== 📞 Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")
    contacts = load_contacts()

    choice = int(input())

    if choice == 1:
        name = input("Enter name of contact: ")
        num = input("Enter contact number (11 Digits): ")
        pattern = r"^\w+[\w\.-]*@\w+[\w\.-]*\.\w{2,3}$"
        valid_number = len(num) == 11 and num.isdigit()
         
        if not valid_number:   
            print("❌  Number should be of 11 digits !!!")
        elif valid_number:
            email = input("Enter a valid email: ")
            valid_email = re.match(pattern, email)
            if not valid_email:
                print("❌  Invalid Email !!!")
            elif valid_email:
                newcontact = {
                    "name" : name,
                    "Contact Number" : num,
                    "Email Address":email 
                }
                contacts.append(newcontact)
                file = open("contacts.json","w")
                json.dump(contacts, file, indent=4)
                file.close()
                print("✅ Contact saved successfully!")

    elif choice == 2:
        count = 0
        print("ALL Contacts:")
        for con in contacts:
            count+=1
            print("ID: ",count,"  Name: ",con["name"])
            print("Contact Number: ",con["Contact Number"])
            print("Email Address: ",con['Email Address'],"\n\n")
    elif choice == 3:
        sel = input("Enter contact number for searching: ")
        print("Selected Contact:")
        for con in contacts:
            if con["Contact Number"] == sel:
                print("Name: ",con["name"])
                print("Contact Number: ",con["Contact Number"])
                print("Email Address: ",con['Email Address'])
                break
        else:
            print("❌ Error: Contact not found.")
               
    elif choice == 4:
        print("Thankyou for using contact book")
        break
    else:
        print("Incorrect choice !!!")
    




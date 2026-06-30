import json

def add_contact():
    print("Adding Contact")
    name = input("Name: ")
    phone_num = input("Phone Number: ")
    email = input("Email: ")

    # phone number and email validation
    if not phone_num.isdigit():
        print("Please enter a valid phone number ex. (+123 456 78910)")

    if "@" not in email:
        print("Please enter a valid email.")

    contacts = {
        "name": name,
        "phone": phone_num,
        "email": email
    }

    # creates contacts.json
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def view_contacts():
    pass

def delete_contact():
    pass

def main():
    while True:
        print("////////////////////////////")
        print("Choose an between (1-4): ")
        print("1) View All Contacts")
        print("2) Add Contact")
        print("3) Delete Contact by Name")
        print("4) Quit")
        print("////////////////////////////")

        user_input = input("Choose an action: ")

        if not user_input.isdigit() or int(user_input) > 4:
            print("******************************")
            print("Please enter between (1-4)!!!")
            print("******************************")
        
        if user_input == "1":
            view_contacts()
        if user_input == "2":
            add_contact()
        if user_input == "3":
            delete_contact()
        if user_input == "4":
            break
        
if __name__ == "__main__":
    main()

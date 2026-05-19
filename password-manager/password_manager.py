from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # with = automaticly closes the file, open() = opens a file
    # r = read mode, a = append mode, w = write mode
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n") # \n new line


while True:
    mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
    if mode == "q":
        break

    if mode == 'view':
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
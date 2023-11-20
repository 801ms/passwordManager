from cryptography.fernet import Fernet

import keyGen

pwd = ""

masterPwd = input("Enter the master password: ")

def keyGeneratedCheck():
    with open("keyGeneratedCheck.txt", "r") as f:
        checkBool = f.readline()
        if checkBool == "True":
            checkBool = True
            print("Key already generated. Prepare to enter generated key to decrypt files.")
        else:
            checkBool = False
            with open("keyGeneratedCheck.txt", "a") as f:
                f.write("True")



def encrypt():
    token = key.encrypt(pwd)
    token

#https://stackoverflow.com/questions/41029991/imported-variable-is-not-defined

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: ", user)
            print("Password: ", passw)
            print("\n")

def add():
    name = input("Enter account name: ")
    pwd = input("Password: ")
    pwd = encrypt()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Add Password or View Existing? (view, add) Press q to quit: ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invald input. Try again.")
        continue
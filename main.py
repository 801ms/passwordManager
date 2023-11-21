from cryptography.fernet import Fernet

masterPwd = input("Enter the master password: ")

def keyGeneratedCheck():
    with open("keyGeneratedCheck.txt", "r") as f:
        checkText = f.read()
        if checkText == "True":
            checkBool = True
            print("Key already generated. Prepare to enter generated key to decrypt files.")
        else:
            checkBool = False
            writeKey()
            with open("keyGeneratedCheck.txt", "w") as f:
                checkBoolOverwrite = checkText.replace("False", "True")
                f.write(checkBoolOverwrite)

def writeKey():
    key = Fernet.generate_key()
    print(key)
    with open ("key.key", "wb") as keyFile:
        keyFile.write(key)

keyGeneratedCheck()

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
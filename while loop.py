print("==== HCL Technologies===")
correct_username = "raga"
correct_password = "123"

while True:   
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break   
    else:
        print("Incorrect username or password! Try again.\n")

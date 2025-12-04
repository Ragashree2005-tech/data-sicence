username = input("Enter username: ")
password = input("Enter password: ")

# Special characters list
special_chars = "!@#$%^&*()_+-={}[]|:;<>,.?/~`"

# Check conditions
if username == "admin":
    if any(char in special_chars for char in password):
        print("Login successful!")
    else:
        print("Password must contain at least one special character.")
else:
    print("Invalid username!")
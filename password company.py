
print("=== HCL Technologies ===")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "java" and password == "123":
    print("Login successful! Welcome to java Department.")

elif username == "python" and password == "456":
    print("Login successful! Welcome to python Department.")

elif username == "Cloud Computing" and password == "789":
    print("Login successful! Welcome to Cloud Computing.")

elif username == "Cybersecurity" and password == "0112":
    print("Login successful! Welcome to Cybersecurity.")

elif username == "website" and password == "2131":
    print("Login successful! Welcome to website Department.")
    
else:
    print("Invalid username or password! Access Denied.")


correct_username="userabc"
correct_password="password123"
entered_username=input("enter your username")
entered_password=input("enter your password")
if entered_username==correct_username and entered_password==correct_password:
    print("login successful!welcome")
else:
    print("Invalid username or password. Please try again.")


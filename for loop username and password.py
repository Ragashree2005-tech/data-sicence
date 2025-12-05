print("=== HCL Technologies ====")
correct_username = "ragashree"
correct_password = "123"
max_attempts = 3

for attempt in range(max_attempts):
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_username == correct_username and entered_password == correct_password:
        print("Login successful! Welcome.")
        break  
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Incorrect username or password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Incorrect username or password.")
            print("Too many incorrect attempts. Account locked.")
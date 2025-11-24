# Brute Force Attack Simulation - Basic Version

correct_password = "12345"

password = input("Enter the password: ")

# Keep asking until the correct password is entered
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")

print("Access granted. Correct password entered.")

# Brute Force Attack Simulation - Advanced Version (5 Attempts)

correct_password = "12345"
attempts_left = 5

while attempts_left > 0:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted. Correct password entered.")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect password. Attempts remaining: {attempts_left}")
        else:
            print("Maximum attempts reached. Authorities have been alerted!")
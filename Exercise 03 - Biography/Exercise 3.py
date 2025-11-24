# Biography Program

# Ask the user for their details
name = input("Enter your full name: ")        # Handles multiple words automatically
hometown = input("Enter your hometown: ")

# Validate the age input to avoid errors if a non-number is entered
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():            # Checks that age contains only digits
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

# Store details in a dictionary
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print the details on separate lines using one print() statement
print(f"{bio['name']}\n{bio['hometown']}\n{bio['age']}")
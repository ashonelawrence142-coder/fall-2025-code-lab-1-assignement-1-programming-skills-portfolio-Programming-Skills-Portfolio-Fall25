# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    # Ask the user for input
    user_input = input("Enter a number: ")
    
    # Validate that the input is a number
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        num = int(user_input)
        # Call the function and get the message
        message = check_even_odd(num)
        # Print the message
        print(message)
    else:
        print("Invalid input. Please enter an integer.")

# Entry point
if __name__ == "__main__":
    main()
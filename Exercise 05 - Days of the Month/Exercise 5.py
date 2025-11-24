# Days of the Month - Advanced Version (Leap Year Adjustment)

# Dictionary mapping month numbers to days
days_in_month = {
    1: 31,
    2: 28,   # February will adjust for leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def main():
    month = input("Enter a month number (1–12): ")

    # Validate that input is a number
    if month.isdigit():
        month = int(month)

        if 1 <= month <= 12:
            # Special case for February
            if month == 2:
                leap = input("Is it a leap year? (yes/no): ").strip().lower()
                if leap == "yes":
                    print("Number of days in February: 29")
                else:
                    print("Number of days in February: 28")
            else:
                print(f"Number of days in month {month}: {days_in_month[month]}")
        else:
            print("Invalid month number. Please choose from 1 to 12.")
    else:
        print("Invalid input. Please enter a number.")

# Entry point
if __name__ == "__main__":
    main()
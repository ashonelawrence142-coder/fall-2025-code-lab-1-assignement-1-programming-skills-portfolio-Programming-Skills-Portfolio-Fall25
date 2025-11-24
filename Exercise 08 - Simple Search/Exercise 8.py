# Simple Search - Full Version (with optional user input)

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def main():
    # Ask user for search term (optional requirement)
    search_term = input("Enter the name you want to search for: ").strip()

    # Check if the search term is in the list
    if search_term in names:
        print(f"{search_term} was found in the list!")
    else:
        print(f"{search_term} was NOT found in the list.")

# Entry point
if __name__ == "__main__":
    main()
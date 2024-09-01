def main():
    numbers = []

    # Collect numbers from the user
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        # Check if the user entered an empty string to quit
        if user_input == "":
            break

        try:
            # Convert the input to a float and add it to the list
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            # Handle the case where the input is not a valid number
            print("Invalid input. Please enter a valid number.")

    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Get the five greatest numbers
    greatest_numbers = numbers[:5]

    # Print out the five greatest numbers
    print("The five greatest numbers are:")
    for number in greatest_numbers:
        print(number)

if __name__ == "__main__":
    main()

def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer.
    
    Returns:
        int: A validated non-negative integer input from the user.
    """
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter a non-negative integer: ")
            # Convert input to an integer
            n = int(user_input)
            # Check if the number is non-negative
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                return n
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    
    Args:
        n (int): The non-negative integer for which the factorial is to be calculated.
    
    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1  # Base case: 0! = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    """
    Main function to execute the program.
    It gets a non-negative integer from the user, calculates its factorial, and displays the result.
    """
    # Get a valid non-negative integer input from the user
    n = get_non_negative_integer()
    
    # Calculate the factorial of the number
    result = calculate_factorial(n)
    
    # Display the result
    print(f"The factorial of is: {result}")

if __name__ == "__main__":
    main()

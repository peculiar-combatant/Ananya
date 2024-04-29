
def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): The number to calculate factorial for.
        
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.
    
    Args:
        n (int): The number of terms in the Fibonacci sequence.
        
    Returns:
        list: The Fibonacci sequence.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    # Calculate factorial
    fact = factorial(num)
    print(f"Factorial of {num} is: {fact}")

    # Calculate Fibonacci sequence
    fib_sequence = [fibonacci(i) for i in range(num)]
    print(f"Fibonacci sequence of {num} numbers is: {fib_sequence}")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    # Calculate factorial
    fact = factorial(num)
    print(f"Factorial of {num} is: {fact}")

    # Calculate Fibonacci sequence
    fib_sequence = [fibonacci(i) for i in range(num)]
    print(f"Fibonacci sequence of {num} numbers is: {fib_sequence}")

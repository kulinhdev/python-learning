# Find fibonacci a number (2 ways) #


# Using generator
def fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)


def get_fibonacci_number(n):
    return list(fibonacci(n))[n]


n = 10
fibonacci_number = get_fibonacci_number(n)
print(f"The {n}th Fibonacci generator number is: {fibonacci_number}")


# Using recursive
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


fibonacci_recursive_number = fibonacci_recursive(n)
print(f"The {n}th Fibonacci recursive number is: {fibonacci_recursive_number}")

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    result = a / b
    return result

numerator = 10
denominator = 0

result = divide_numbers(numerator, denominator)
print(f"Result: {result}")

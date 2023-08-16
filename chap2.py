from contextlib import suppress

# Example function that might raise an exception
def divide(a, b):
    return a / b

# Using contextlib.suppress to handle a specific exception gracefully
def safe_divide(a, b):
    with suppress(ZeroDivisionError):
        result = divide(a, b)
        return result
    return None

# Example usage
numerator = 10
denominator = 0

result = safe_divide(numerator, denominator)
if result is None:
    print("Division by zero occurred, but it was handled gracefully.")
else:
    print("Result:", result)

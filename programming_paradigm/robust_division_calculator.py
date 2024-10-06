def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    except TypeError:
        return f"Error: Please enter numeric values only."

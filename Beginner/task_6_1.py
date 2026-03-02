"""
Topic: Rounding & Power (Task 6.1)

Syntax:
    import math
    ceil_val = math.ceil(number)
    floor_val = math.floor(number)
    power_val = math.pow(base, exponent)

Example:
    val = math.ceil(4.2)  # 5
    res = math.pow(2, 3)  # 8.0

I/O:
    Input: A floating-point number from user input.
    Output: Print its ceiling, floor, and the number raised to the power of 2.
"""

# TODO: Import the 'math' module.
# TODO: Ask the user to input a floating-point number.
# TODO: Calculate the ceiling, floor, and square (power of 2).
# TODO: Print all three results with clear labels.
import math


def solution() -> None:
    """Take input from user and print Ceiling, Floor, and Square."""
    float_number: float = float(input("Enter a float number: "))
    print(f"ceiling: {math.ceil(float_number)}, floor: {math.floor(float_number)}, square: {math.pow(float_number, 2) :.2f}")


if __name__ == "__main__":
    solution()
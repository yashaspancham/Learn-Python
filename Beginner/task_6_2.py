"""
Topic: Constants (Task 6.2)

Syntax:
    pi_val = math.pi
    e_val = math.e

Example:
    print(math.pi)  # 3.141592653589793

I/O:
    Input: None.
    Output: Print the values of Pi and Euler's number (e) from the math module.
"""

# TODO: Import the 'math' module.
# TODO: Access 'math.pi' and 'math.e'.
# TODO: Print both constants to 5 decimal places using f-strings.
import math


def solution() -> None:
    """Print pi and e."""
    print(f"pi: {math.pi :.5f}, e: {math.e :.5f}")


if __name__ == "__main__":
    solution()
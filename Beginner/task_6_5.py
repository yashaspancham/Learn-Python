"""
Topic: Random Ranges (Task 6.5)

Syntax:
    import random
    number = random.uniform(low, high)  # returns a float between low and high

Example:
    value = random.uniform(1.0, 10.0)
    # value could be 4.327891...

I/O:
    Input: None (hardcoded range 1.0 to 10.0).
    Output: Print the generated float.
"""

# TODO: Import the 'random' module.
# TODO: Use 'random.uniform()' to generate a float between 1.0 and 10.0.
# TODO: Print the result.
import random


def solution() -> None:
    """Generate a random float between 1 and 10."""
    print(f"Random float: {random.uniform(1.0, 10.0)}")


if __name__ == "__main__":
    solution()
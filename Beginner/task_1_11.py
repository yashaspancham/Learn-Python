"""
Topic: Dictionary Comprehensions (Task 1.11)

Syntax:
    {key_expr: value_expr for item in iterable if condition}

Example:
    evens_squared = {x: x**2 for x in range(10) if x % 2 == 0}

I/O:
    Input: A range of integers (e.g., 1 to 10).
    Output: A dictionary mapping each integer to its square.
"""

def generate_squares(start: int, end: int) -> dict[int, int]:
    """Generates a dictionary of numbers and their squares using comprehension.

    Args:
        start: The beginning of the range (inclusive).
        end: The end of the range (inclusive).

    Returns:
        A dictionary where keys are numbers and values are their squares.
    """
    # TODO: Implement dictionary comprehension here
    if end <= start:
        raise ValueError("Error: condition end > start not met")
    numbers_and_squares: dict[int, int] = { i: i**2 for i in range(start, end + 1) }
    return numbers_and_squares

if __name__ == "__main__":
    # TODO: Call generate_squares with range 1 to 10 and print the result
    print(generate_squares(1, 10))

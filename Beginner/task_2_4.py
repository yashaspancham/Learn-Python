"""
Topic: Reverse Slicing (Task 2.4)

Syntax:
    reversed_item = item[::-1]

Example:
    text = "Python"
    backwards = text[::-1]  # "nohtyP"

I/O:
    Input: A string "Hello World".
    Output: Reverse the string using a negative step slice and print it.
"""

# TODO: Define a string variable 'message' with the value "Hello World".
# TODO: Use the negative step slice [::-1] to reverse the string.
# TODO: Print the reversed result to verify it matches "dlroW olleH".


def solution() -> None:
    """Create a string and reverse it."""
    message: str = "Hello World"
    print(message[::-1])


if __name__ == "__main__":
    solution()
"""
Topic: Search & Count (Task 2.9)

Syntax:
    index = my_tuple.index(value)
    occurrence = my_tuple.count(value)

Example:
    data = (1, 2, 2, 3)
    idx = data.index(2)  # 1
    cnt = data.count(2)  # 2

I/O:
    Input: A tuple of repeating numbers.
    Output: Find the first index of a value and its total count.
"""

# TODO: Define a tuple 'numbers' with at least 10 values, including duplicates.
# TODO: Find the index of a specific value that appears multiple times.
# TODO: Count how many times that same value appears in the tuple.
# TODO: Print both the index and the count with descriptive labels.


def solution() -> None:
    """Create a tuple, given a number print its index and count."""
    numbers: tuple[int, ...] = (0, 1, 2, 10, 4, 5, 6, 7, 8, 9, 2, 3, 2, 3)
    number: int = 3
    print(f"Number: {number}, Count: {numbers.count(number)}, First Index: {numbers.index(number)}")


if __name__ == "__main__":
    solution()
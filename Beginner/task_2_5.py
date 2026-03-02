"""
Topic: Step Slicing (Task 2.5)

Syntax:
    subset = items[start:stop:step]

Example:
    nums = [1, 2, 3, 4, 5, 6]
    evens = nums[1::2]  # [2, 4, 6]

I/O:
    Input: A list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    Output: Extract every second element starting from the first and print it.
"""

# TODO: Define a list 'numbers' from 1 to 10.
# TODO: Use step slicing to get every second element (e.g., 1, 3, 5, 7, 9).
# TODO: Print the result to verify it matches [1, 3, 5, 7, 9].


def solution() -> None:
    """Create a list extract every 2nd element."""
    numbers_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers_list[::2])


if __name__ == "__main__":
    solution()
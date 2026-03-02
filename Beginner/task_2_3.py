"""
Topic: Basic Slicing (Task 2.3)

Syntax:
    sub_list = items[start:stop]

Example:
    nums = [10, 20, 30, 40]
    middle = nums[1:3]  # [20, 30]

I/O:
    Input: The list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
    Output: Use slicing to extract [2, 3, 4, 5] and print it.
"""

# TODO: Define a list 'numbers' from 0 to 9.
# TODO: Use slicing to extract the sequence from index 2 up to (but not including) index 6.
# TODO: Print the resulting slice to verify it matches [2, 3, 4, 5].


def solution() -> None:
    """Create a list then extract a part of it."""
    input_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    output_list: list[int] = input_list[2: 6]
    print(output_list)


if __name__ == "__main__":
    solution()
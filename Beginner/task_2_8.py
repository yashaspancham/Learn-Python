"""
Topic: Nested Slicing (Task 2.8)

Syntax:
    subset = matrix[:2]

Example:
    data = [[1, 2], [3, 4], [5, 6]]
    first_two = data[:2]  # [[1, 2], [3, 4]]

I/O:
    Input: A list of at least 4 sub-lists.
    Output: Use slicing to extract the first 2 sub-lists and print them.
"""

# TODO: Create a list 'matrix' with 4 sub-lists (e.g., [1, 2], [3, 4], etc.).
# TODO: Use slicing to extract the first two sub-lists.
# TODO: Print the result to verify the structure remains a list of lists.


def solution() -> None:
    """Create a 2D list and print first two sub-lists."""
    matrix: list[list[int]] = [[1, 2], [3, 5], [5, 7], [8, 0], [10, 11]]
    if len(matrix) < 2:
        print(matrix)
        return None
    print(matrix[:2])


if __name__ == "__main__":
    solution()
"""
Topic: Set Creation (Task 1.6)

Syntax:
    my_set = set(my_list)

Description:
    Converting a list with duplicates to a set automatically removes them.

I/O:
    Input: A list with at least 3 duplicate numbers.
    Output: Print the list, then print the resulting set.
"""

# TODO: Create a list with duplicates.
# TODO: Convert to a set and print.



def solution() -> None:
    """Create a list with 3 duplicate numbers then convert to set then print both."""
    nums_list: list[int] = [2, 2, 2, 5, 6, 89, 89, 89, 89]
    print(f"nums_list: {nums_list}")
    nums_set: set[int] = set(nums_list)
    print(f"nums_set: {nums_set}")




if __name__ == "__main__":
    solution()
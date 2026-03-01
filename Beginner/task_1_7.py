"""
Topic: Set Membership (Task 1.7)

Syntax:
    if element in my_set:
        print("Exists")

Description:
    Sets use hashing to make membership checks (using the 'in' keyword) extremely fast (O(1)).

I/O:
    Input: A set of 5 unique items.
    Output: Check if a specific item exists in the set and print the result.
"""

# TODO: Create a set of 5 unique items.
# TODO: Use the 'in' keyword to check for an item and print the result.


def check_item_in_set(search_value: int, unique_items_set: set[int]) -> None:
    """Checks if an element is in a set and prints it.

    Args:
        search_value: The value to be searched for.
        unique_items_set: The set of values to search within.

    Returns:
        None.
    """
    if search_value in unique_items_set:
        print(search_value)


def solution() -> None:
    """Creates a set with 5 unique items and checks for membership.

    Returns:
        None.
    """
    unique_items_set: set[int] = {2, 4, 6, 1, 10}
    search_value: int = 3
    check_item_in_set(search_value, unique_items_set)
    search_value: int = 4
    check_item_in_set(search_value, unique_items_set)


if __name__ == "__main__":
    solution()

"""
Topic: Immutable Storage (Task 2.1)

Syntax:
    my_tuple = (item1, item2, item3)

Concept:
    Tuples are immutable; once created, their contents cannot be changed.

I/O:
    Input: A tuple representing fixed coordinates (x, y, z).
    Output: Attempt to modify the tuple and handle the resulting TypeError.
"""

# TODO: Create a tuple named 'location' with three integer coordinates.
# TODO: Print the initial location.
# TODO: Try to change the second element of 'location' to a new value.
# TODO: Wrap the modification attempt in a try/except block to catch 'TypeError'.
# TODO: Print a message confirming that tuples are immutable when the error occurs.


def solution() -> None:
    """Create a tuple, try to update it, print the message."""
    location: tuple[int, int, int] = (2, 4, 5)
    print(f"initial location: {location}")
    try: 
        location[0] = 7
        print(f"after update location: {location}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    solution()
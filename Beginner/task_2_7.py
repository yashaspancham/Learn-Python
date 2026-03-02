"""
Topic: Tuple Concatenation (Task 2.7)

Syntax:
    new_tuple = tuple_a + tuple_b

Example:
    pair_1 = (1, 2)
    pair_2 = (3, 4)
    combined = pair_1 + pair_2  # (1, 2, 3, 4)

I/O:
    Input: Two tuples (e.g., coordinates and metadata).
    Output: Combine them into a single tuple and print the result.
"""

# TODO: Define 'base_info' with (ID, Name).
# TODO: Define 'extra_info' with (Role, ActiveStatus).
# TODO: Concatenate them into a new tuple 'full_record'.
# TODO: Print the final combined tuple.


def solution() -> None:
    """Create two tuples, combine & print them."""
    base_info: tuple[str, str] = ("ID", "Name")
    extra_info: tuple[str, str] = ("Role", "ActiveStatus")
    full_record: tuple[str, ...] = base_info + extra_info
    print(full_record)


if __name__ == "__main__":
    solution()
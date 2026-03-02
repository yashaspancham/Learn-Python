"""
Topic: Tuple Unpacking (Task 2.2)

Syntax:
    a, b, c = (1, 2, 3)

Example:
    point = (10, 20)
    x, y = point

I/O:
    Input: A tuple (10, 20, 30).
    Output: Assign items to variables 'a', 'b', and 'c' and print them.
"""

# TODO: Create a tuple named 'data' with values 10, 20, 30.
# TODO: Unpack the tuple into variables 'a', 'b', and 'c' in one line.
# TODO: Print each variable to verify the unpacking.
# TODO: (Extra) Demonstrate unpacking a tuple while ignoring a value using '_'.


def solution() -> None:
    """Create a tuple, unpack and print."""
    data: tuple[int, int, int] = (10, 20, 30)
    a, b, c = data
    print(f"a: {a}, b: {b}, c: {c}")
    print("Skipping values task")
    a, _, c = data
    print(f"a: {a}, c: {c}")


if __name__ == "__main__":
    solution()
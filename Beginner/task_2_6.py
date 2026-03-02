"""
Topic: Last N Elements (Task 2.6)

Syntax:
    last_three = items[-3:]

Example:
    names = ["Alice", "Bob", "Charlie", "Dave"]
    last_two = names[-2:]  # ["Charlie", "Dave"]

I/O:
    Input: Any list of at least 5 elements.
    Output: Use slicing to get exactly the last 3 elements and print them.
"""

# TODO: Define a list 'fruits' with at least 5 different strings.
# TODO: Use negative slicing to extract only the last 3 items.
# TODO: Print the resulting slice to verify it works for any list length.


def solution() -> None:
    """Create a list, then extract the last 3 items."""
    fruits: list[str] = ["apple", "pineapple", "watermelon", "melon", "blueberry", "blackberry", "banana"]
    if len(fruits) < 3:
        print(fruits)
        return
    print(fruits[-3:])


if __name__ == "__main__":
    solution()
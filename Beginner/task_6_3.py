"""
Topic: Random Choice (Task 6.3)

Syntax:
    import random
    picked = random.choice(sequence)

Example:
    names = ["Alice", "Bob"]
    winner = random.choice(names)

I/O:
    Input: A list of 5 names.
    Output: Pick one name randomly and print it.
"""

# TODO: Import the 'random' module.
# TODO: Create a list 'names' with 5 strings.
# TODO: Use 'random.choice()' to pick a random name.
# TODO: Print the winner with a celebratory message.
import random


def solution() -> None:
    """Create a list and pick one element at random."""
    names: list[str] = ["Alice", "Bob", "Jim", "John", "Joe"]
    winner: str = random.choice(names)
    print(f"And the winner is.............{winner}")


if __name__ == "__main__":
    solution()

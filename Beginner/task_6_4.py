"""
Topic: Shuffling (Task 6.4)

Syntax:
    import random
    random.shuffle(list)  # modifies list in place, returns None

Example:
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)
    # items is now reordered, e.g. [3, 1, 5, 2, 4]

I/O:
    Input: A list of 5 tasks (strings).
    Output: Print the list before and after shuffling.
"""

# TODO: Import the 'random' module.
# TODO: Create a list 'tasks' with 5 task strings.
# TODO: Print the original list.
# TODO: Use 'random.shuffle()' to reorder the list in place.
# TODO: Print the shuffled list.
import random


def solution() -> None:
    """Create a list then shuffle it."""
    tasks: list[str] = ["Ace", "King", "Queen", "Joker", "Minister"]
    print(f"tasks: {tasks}")
    random.shuffle(tasks)
    print(f"shuffled_task: {tasks}")


if __name__ == "__main__":
    solution()
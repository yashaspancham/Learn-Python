"""
Topic: Sorting by Value (Task 1.15)

Syntax:
    sorted_items = sorted(my_dict.items(), key=lambda item: item[1])

Example:
    scores = {"Alice": 88, "Bob": 95}
    ranked = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

I/O:
    Input: A dictionary of products and their prices.
    Output: A list of product names sorted from cheapest to most expensive.
"""

# TODO: Define a dictionary 'inventory' with at least 5 products and prices.
# TODO: Use the 'sorted()' function with a 'lambda' to sort by price.
# TODO: Implement a function 'get_sorted_products' that returns only the names.
# TODO: Ensure the function has proper type hints and a Google-style docstring.
# TODO: Print the final sorted list in the 'if __name__ == "__main__":' block.


def get_sorted_products(items: dict[str, int]) -> dict[str, int]:
    """Sort dict based on price.

    Args:
        items: Product and price as key and value.

    Returns: Product and price as key and value sorted by price.
    """
    sorted_items: dict[str, int] = sorted(items.items(), key=lambda item: item[1])
    return dict(sorted_items)


def solution() -> None:
    """Create a dict then sort and print it."""
    items: dict[str, int] = {
        "Apple": 88, "Banana": 95, "Cherry": 73, "Watermelon": 99, "John": 86, "James": 56, "Charlie": 45
    }
    print(f"items: {items}")
    sorted_items: dict[str, int] = get_sorted_products(items)
    print(f"sorted_items: {sorted_items}")


if __name__ == "__main__":
    solution()
"""
Topic: Mathematical Set Operations (Task 1.8)

Syntax:
    union_set = set_a | set_b         # or set_a.union(set_b)
    intersection_set = set_a & set_b  # or set_a.intersection(set_b)

Description:
    Sets support standard mathematical operations. Union combines all unique items, 
    while intersection finds items present in both.

I/O:
    Input: Two sets with some common and some unique elements.
    Output: Print the union and then print the intersection.
"""

# TODO: Create two sets (set_a and set_b).
# TODO: Calculate and print the union (|).
# TODO: Calculate and print the intersection (&).


def solution() -> None:
    """Create two sets with some common elements then calculate and print union and intersection.
    """
    set_a: set[int] = {1, 2, 3, 4, 5, 6}
    set_b: set[int] = {5, 6, 7, 8, 9, 10}
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")


if __name__ == "__main__":
    solution()
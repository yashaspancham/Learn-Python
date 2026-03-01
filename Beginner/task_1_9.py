"""
Topic: Difference vs Symmetric Difference (Task 1.9)

Syntax:
    diff = set_a - set_b             # Items in A but NOT in B
    sym_diff = set_a ^ set_b         # Items in A or B but NOT both

Description:
    'Difference' is directional (A-B is different from B-A).
    'Symmetric Difference' finds unique items from both sets combined.

I/O:
    Input: Two sets (e.g., students in Math class vs students in Science class).
    Output: Print the difference (A-B) and then print the symmetric difference.
"""

# TODO: Create set_a and set_b.
# TODO: Calculate and print the difference (A - B).
# TODO: Calculate and print the symmetric difference (^).


def solution() -> None:
    """Create two sets, then calculate and print difference(A - B) and symmetric difference."""
    set_a: set[int] = {1, 2, 3, 4, 5, 6}
    set_b: set[int] = {5, 6, 7, 8, 9, 10}
    print(f"diff: {set_a - set_b}")
    print(f"symmetric diff: {set_a ^ set_b}")


if __name__ == "__main__":
    solution()
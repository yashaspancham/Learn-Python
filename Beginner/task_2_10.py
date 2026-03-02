"""
Topic: The Password Generator (Task 2.10)

Syntax:
    subset = population[start:stop:step]

Example:
    pool = "abcdefgh"
    part = pool[1:5:2]  # "bd"

I/O:
    Input: A long string of characters (letters, digits, symbols).
    Output: Use various slices to pick pieces and combine them into a password.
"""

# TODO: Define a string 'pool' with at least 50 mixed characters.
# TODO: Extract three different pieces using different slicing techniques (e.g., [:5], [-5:], [::7]).
# TODO: Concatenate these pieces to form a 10-15 character password.
# TODO: Print the generated password.


import string


def solution() -> None:
    """Create a string pool, generate and print password."""
    string_pool: str = string.punctuation + "₹©®™±×÷√∞∆≈≠≤≥" + string.digits + string.ascii_letters
    password: str = string_pool[20::-30] + string_pool[-20::-10] + string_pool[:40:-16]
    print(password)


if __name__ == "__main__":
    solution()
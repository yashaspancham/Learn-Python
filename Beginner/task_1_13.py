"""Task 1.13: Dictionary Merging.

This module demonstrates the use of the dictionary merge operator `|` 
(introduced in Python 3.9) to combine multiple dictionaries into a new one.

Syntax:
    merged_dict = dict_a | dict_b

Examples:
    >>> primary_colors = {"red": "#FF0000", "blue": "#0000FF"}
    >>> secondary_colors = {"green": "#00FF00", "yellow": "#FFFF00"}
    >>> all_colors = primary_colors | secondary_colors
    >>> print(all_colors)
    {'red': '#FF0000', 'blue': '#0000FF', 'green': '#00FF00', 'yellow': '#FFFF00'}

Note:
    If both dictionaries contain the same key, the value from the right-hand 
    dictionary (`dict_b`) takes precedence.
"""

# TODO: Define a dictionary named 'user_profile' with 'name' and 'role' keys.
# TODO: Define a dictionary named 'user_settings' with 'theme' and 'notifications' keys.
# TODO: Use the '|' operator to merge them into a new dictionary 'full_account'.
# TODO: Print 'full_account' and verify it contains all four keys.
# TODO: (Optional) Create a third dictionary that overrides one existing key and merge it.


def solution():
    """Create two dicts, combine into 3ed, combine it with 4th.
    """
    user_profile: dict[str, str] = {
        "name": "Ferris",
        "role": "Rustacean"
    }
    user_settings: dict[str, str | bool] = {
        "theme": "dark",
        "notifications": True
    }
    new_user_profile: dict[str, str] = {
        "meta": "www.github.com/repo_name",
        "name": "New_Ferris",
    }
    full_account: dict[str, str | bool] = user_profile | user_settings
    print(f"First combined dict: {full_account}")
    optional_dict: dict[str, str | bool] = full_account | new_user_profile
    print(f"optional_part: {optional_dict}")


if __name__ == "__main__":
    solution()
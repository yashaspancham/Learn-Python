"""
Topic: Nested Dictionaries (Task 1.14)

Syntax:
    nested_value = outer_dict["outer_key"]["inner_key"]
    outer_dict["outer_key"]["inner_key"] = new_value

Example:
    registry = {"user_1": {"name": "Alice", "role": "Admin"}}
    registry["user_1"]["role"] = "Superuser"

I/O:
    Input: A nested dictionary representing a user database.
    Output: Update a specific nested value and return the modified sub-dictionary.
"""

# TODO: Define a dictionary 'user_database' with nested keys for 'id_101' and 'id_102'.
# TODO: Each user ID should map to a dictionary with 'username' and 'is_active' (bool).
# TODO: Implement 'toggle_user_status' to flip the 'is_active' status of a given ID.
# TODO: The function must use type hints for the nested dictionary structure.
# TODO: Print the specific user's updated data in the if __name__ == "__main__": block.



def toggle_user_status(user_data: dict[str, str | bool]) -> dict[str, str | bool]:
    """Toggles is_active and returns user_data.
    
    Args:
        user_data: Dict with username and is_active.
    
    Returns:
        user_data: Dict with username and is_active.
    """
    user_data["is_active"] = not user_data["is_active"] 
    return user_data


def solution() -> None:
    """Create dict user_database, then toggle is_active."""
    user_database: dict[str, dict[str, str | bool]] = {
        'id_101': {
            'username': 'kim',
            'is_active': False
        },
        'id_102': {
            'username': 'Jim',
            'is_active': True
        }
    }
    print(f"before: {user_database}")
    for user_id, user_data in user_database.items():
        user_database[user_id] = toggle_user_status(user_data) 
    print(f"after: {user_database}")


if __name__ == "__main__":
    solution()
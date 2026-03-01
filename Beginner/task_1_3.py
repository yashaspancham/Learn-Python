"""
Topic: Dictionaries - Dynamic Updates (Task 1.3)

Syntax:
    # Adding/Updating
    dictionary_name["key"] = "new_value"

    # Multiple Updates
    dictionary_name.update({"key1": "val1", "key2": "val2"})

Description:
    Dictionaries are mutable. You can add new key-value pairs or change existing ones.

Example:
    user = {"name": "Yashas"}
    user["age"] = 25  # Adds new key
    user["name"] = "Yashas-Dev"  # Updates existing key

I/O:
    Input: An existing dictionary.
    Output: The updated dictionary after adding and modifying keys.
"""

# TODO: Create a dictionary.
# TODO: Add a new key-value pair.
# TODO: Update an existing value.
# TODO: Print the final dictionary.



def solution() -> None:
    """Creating a empty dict then adding values first one at a time then multiple at once"""
    new_dict: dict[str, float] = {
        "King": 10.0,
        "Queen": 5.5
    }
    print(f"before: {new_dict}")
    new_dict["Prince"] = 13.3
    new_dict["King"] = 11.11
    print(f"after: {new_dict}")




if __name__ == "__main__":
    solution()
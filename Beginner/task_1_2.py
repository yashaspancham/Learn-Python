"""
Topic: Dictionaries - Safe Retrieval (Task 1.2)

Syntax:
    value = dictionary_name.get("key", default_value)

Description:
    The .get() method returns the value for a key if it exists.
    If not, it returns None (or a specified default) instead of raising a KeyError.

Example:
    scores = {"Alice": 10}
    print(scores.get("Bob"))        # Output: None
    print(scores.get("Bob", 0))     # Output: 0

I/O:
    Input: A key that does not exist in the dictionary.
    Output: A safe message or a default value.
"""

# TODO: Create a dictionary.
# TODO: Use .get() to retrieve a missing key without crashing.
# TODO: Print the result.





def solution() -> None:
    """ Create dict then if look for value of a key which does not exist and print a default value"""
    default_dict_value: int = -1
    my_dict: dict[str, int] = {
        "Alice": 10,
        "Bob": 20,
        "Charlie": 30
    }
    no_value:int | None = my_dict.get("Joe", default_dict_value)
    print(no_value)




if __name__ == "__main__":
    solution()
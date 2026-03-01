"""
Topic: Dictionary Iteration (Task 1.4)

Syntax:
    for key in dictionary:
        print(key)
    
    for val in dictionary.values():
        print(val)

Description:
    By default, iterating over a dictionary loops through its keys.
    To iterate over values specifically, use .values().

Example:
    colors = {"red": "#FF0000", "green": "#00FF00"}
    for name in colors: print(name)  # red, green

I/O:
    Input: A dictionary with at least 3 pairs.
    Output: First print all keys, then print all values.
"""

# TODO: Create a dictionary.
# TODO: Loop and print all keys.
# TODO: Loop and print all values.


def solution() -> None:
    """Creates a dictionary with 3 key-value pairs
    first prints all keys then prints all values
    """
    age_dict: dict[str, int] = {
        "Bob": 10,
        "Joe": 11,
        "Jane": 45
    }
    print("Printing Keys: ")
    for key in age_dict:
        print(key)
    print("Printing Values: ")
    for value in age_dict.values():
        print(value)




if __name__ == "__main__":
    solution()
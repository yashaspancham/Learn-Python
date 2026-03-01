"""
Topic: Dictionaries - Initialize & Access (Task 1.1)

Syntax:
    dictionary_name = {
        "key1": "value1",
        "key2": "value2"
    }

Accessing:
    value = dictionary_name["key1"]

Example:
    capitals = {"USA": "Washington D.C.", "France": "Paris"}
    print(capitals["USA"])  # Output: Washing   ton D.C.

I/O:
    Input: A string key (e.g., "Python")
    Output: A string value (e.g., "Guido van Rossum")
"""

# TODO: Create a dictionary of 5 programming languages and their creators.
# TODO: Print a specific creator using a key.



def solution() -> None:
    """
    Function creates dict of programming languages and creators and then prints one of them
    here it is c 
    """
    programming_languages_and_creators: dict[str,str] = {
        "c": "Dennis Ritchie",
        "c++": "Bjarne Stroustrup",
        "python": "Guido van Rossum",
        "Rust": "Graydon Hoare",
        "Go": "Robert Griesemer, Rob Pike, and Ken Thompson",
        "Javascript": "Brendan Eich"
    }

    print(programming_languages_and_creators["c"])




if __name__ == "__main__":
    solution()
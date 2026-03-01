"""
Topic: Key-Value Unpacking (Task 1.5)

Syntax:
    for key, value in dictionary.items():
        print(f"{key}: {value}")

Description:
    The .items() method returns a sequence of (key, value) tuples. 
    You can "unpack" these directly in the for-loop header.

I/O:
    Input: A dictionary of 3+ programming languages and their creators.
    Output: Print "The creator of [Language] is [Name]" for each pair.
"""

def solution() -> None:
    """Prints programming languages and their creators using .items()."""
    # TODO: Create the dictionary.
    # TODO: Loop using .items() and print the formatted string.
    programming_languages_and_creators: dict[str, str] = {
        "c": "Dennis Ritchie",
        "c++": "Bjarne Stroustrup",
        "python": "Guido van Rossum",
        "Rust": "Graydon Hoare",
        "Go": "Robert Griesemer, Rob Pike, and Ken Thompson",
        "Javascript": "Brendan Eich"
    }
    for key, value in programming_languages_and_creators.items():
        print(f"The creator of {key} is {value}")




if __name__ == "__main__":
    solution()

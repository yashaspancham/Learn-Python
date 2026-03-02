"""
Topic: Set Comprehensions (Task 1.12)

Syntax:
    {expression for item in iterable if condition}

Example:
    unique_lengths = {len(word) for word in ["apple", "banana", "apple"]}

I/O:
    Input: A list of strings (e.g., ["cat", "apple", "dog", "banana", "kiwi"]).
    Output: A set of uppercase strings for words with length > 3.
"""

# TODO: Implement a function 'process_words' that uses set comprehension.
# TODO: Filter for words > 3 characters and convert them to uppercase.
# TODO: Use the 'if __name__ == "__main__":' block to call the solution.


def process_words(string_list: list[str]) -> set[str]:
    """Convert list to set then filter only strings with length > 3 then convert them to uppercase.
    
    Args:
        String_list: list of strings to be filtered.

    Returns:
        Filtered_set: set of strings which have more than 3 characters and are uppercase.
    """
    return {word.upper() for word in string_list if len(word) > 3}


if __name__ == "__main__":
    string_list: list[str] = ["cat", "apple", "dog", "banana", "kiwi"]
    print(process_words(string_list))
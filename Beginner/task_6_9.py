"""
Topic: Formatting Dates (Task 6.9)

Syntax:
    import datetime
    now = datetime.datetime.now()
    formatted = now.strftime(format_string)

Example:
    now = datetime.datetime.now()
    print(now.strftime("%A, %B %d, %Y"))
    # Output: Monday, March 02, 2026

I/O:
    Input: None.
    Output: Print the current date in the format: "Friday, February 28, 2026".
"""

# TODO: Import the 'datetime' module.
# TODO: Get the current date and time using 'datetime.datetime.now()'.
# TODO: Format it using 'strftime()' with the pattern: "%A, %B %d, %Y".
# TODO: Print the formatted string.
import datetime


def solution() -> None:
    """Print todays date in Friday, February 28, 2026 format."""
    print(datetime.datetime.now().strftime("%A, %B %d, %Y"))


if __name__ == "__main__":
    solution()

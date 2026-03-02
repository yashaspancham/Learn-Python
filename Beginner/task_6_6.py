"""
Topic: Current Time (Task 6.6)

Syntax:
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("format_string"))

Example:
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    # Output: 2026-03-02 14:30:00

I/O:
    Input: None.
    Output: Print the current date and time in a readable format.
"""

# TODO: Import the 'datetime' module.
# TODO: Get the current date and time using 'datetime.datetime.now()'.
# TODO: Print it in a readable format using 'strftime()'.
import datetime


def solution() -> None:
    """Print the current time in human readable form."""
    print(f"Current time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")


if __name__ == "__main__":
    solution()

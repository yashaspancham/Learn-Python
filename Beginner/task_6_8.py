"""
Topic: Parsing Dates (Task 6.8)

Syntax:
    import datetime
    date = datetime.datetime.strptime(date_string, format_string)

Example:
    date = datetime.datetime.strptime("2026-12-25", "%Y-%m-%d")
    print(date)
    # Output: 2026-12-25 00:00:00

I/O:
    Input: A hardcoded string "2026-12-25".
    Output: Print the parsed datetime object.
"""

# TODO: Import the 'datetime' module.
# TODO: Define a string variable with value "2026-12-25".
# TODO: Use 'datetime.datetime.strptime()' to parse it into a datetime object.
# TODO: Print the result.
import datetime


def solution() -> None:
    """Convert datetime string to datetime.datetime object."""
    datetime_string: str = "2026-12-25"
    parsed_datetime: datetime.datetime = datetime.datetime.strptime(datetime_string, "%Y-%m-%d")
    print(parsed_datetime)


if __name__ == "__main__":
    solution()
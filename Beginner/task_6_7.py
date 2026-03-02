"""
Topic: Date Arithmetic (Task 6.7)

Syntax:
    import datetime
    today = datetime.date.today()
    future = today + datetime.timedelta(days=100)

Example:
    today = datetime.date.today()
    future = today + datetime.timedelta(days=100)
    print(future)
    # Output: 2026-06-10 (example)

I/O:
    Input: None (hardcoded 100 days).
    Output: Print the date exactly 100 days from today.
"""

# TODO: Import the 'datetime' module.
# TODO: Get today's date using 'datetime.date.today()'.
# TODO: Add 100 days using 'datetime.timedelta(days=100)'.
# TODO: Print the resulting date.
import datetime


def solution() -> None:
    """Get today'date then go 100 days to future."""
    today: datetime.date = datetime.date.today()
    print(f"today: {today}")
    future: datetime.date = today + datetime.timedelta(days=100)
    print(f"future: {future}")


if __name__ == "__main__":
    solution()
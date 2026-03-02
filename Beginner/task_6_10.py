"""
Topic: The Birthday Countdown (Task 6.10)

Syntax:
    import datetime
    today = datetime.datetime.now()
    birthday = datetime.datetime(year, month, day)
    delta = birthday - today
    delta.days        # total days remaining
    delta.seconds     # remaining seconds in the last partial day

Example:
    today = datetime.datetime.now()
    birthday = datetime.datetime(2026, 12, 25)
    delta = birthday - today
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

I/O:
    Input: User enters their birthday as "YYYY-MM-DD".
    Output: Print the days, hours, and minutes remaining until the next birthday.
"""

# TODO: Import the 'datetime' module.
# TODO: Ask the user to input their birthday in "YYYY-MM-DD" format.
# TODO: Parse the input string into a datetime object using 'strptime()'.
# TODO: Build this year's birthday using the parsed month and day.
# TODO: If this year's birthday has already passed, use next year's birthday.
# TODO: Calculate the timedelta between now and the birthday.
# TODO: Extract days, hours, and minutes from the delta.
# TODO: Print the countdown in a readable format.
import datetime


def solution() -> None:
    """Take user birthday and calculate remaining time."""
    today: datetime.datetime = datetime.datetime.now()
    birthday_string: str = input("Enter your birthday (YYYY-MM-DD): ")
    try:
        user_bday: datetime.datetime = datetime.datetime.strptime(birthday_string, "%Y-%m-%d")
        this_year_bday: datetime.datetime = user_bday.replace(year=today.year)
        if this_year_bday < today:
            print("That date has passed this year; calculating for next year's birthday.")
            target_date: datetime.datetime = this_year_bday.replace(year=today.year + 1)
        else:
            target_date = this_year_bday
        countdown_delta: datetime.timedelta = target_date - today
        days: int = countdown_delta.days
        hours: int = countdown_delta.seconds // 3600
        minutes: int = (countdown_delta.seconds % 3600) // 60
        print(f"Time remaining: {days} days, {hours} hours, and {minutes} minutes.")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")


if __name__ == "__main__":
    solution()
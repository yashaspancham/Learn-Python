# Beginner Mastery Tasks

## 1. Dictionaries & Sets
1. **[DONE] Initialize & Access:** Create a dictionary of 5 programming languages and their creators. Print a specific creator using a key.
2. **[DONE] Safe Retrieval:** Use the `.get()` method to retrieve a key that doesn't exist without crashing the program.
3. **[DONE] Dynamic Updates:** Add a new key-value pair to an existing dictionary and then update an existing value.
4. **[DONE] Dictionary Iteration:** Loop through a dictionary and print only the keys, then loop again to print only the values.
5. **[DONE] Key-Value Unpacking:** Use `.items()` in a `for` loop to print "The creator of [Language] is [Name]".
6. **[DONE] Set Creation:** Create a list with duplicate numbers and convert it into a `set` to automatically remove duplicates.
7. **[DONE] Set Membership:** Check if a specific element exists in a set using the `in` keyword (fast lookup).
8. **[DONE] Mathematical Set Operations:** Create two sets and find their `union` (all items) and `intersection` (common items).
9. **[DONE] Difference vs Symmetric Difference:** Find items present in set A but not B, then items present in either A or B but not both.
10. **[DONE] The Flashcard App:** Build a CLI tool where users are quizzed on dictionary keys. Use a set to track which questions they got wrong.
11. **[DONE] Dictionary Comprehensions:** Create a dictionary of `{x: x**2}` for a range of 1 to 10.
12. **[DONE] Set Comprehensions:** Create a set of uppercase strings from a list of words, filtering for words longer than 3 characters.
13. **[DONE] Dictionary Merging:** Use the `|` merge operator (Python 3.9+) to combine two dictionaries into a third.
14. **[DONE] Nested Dictionaries:** Access and update a value inside a multi-level dictionary (e.g., a dictionary of users).
15. **[DONE] Sorting by Value:** Use the `sorted()` function with a `lambda` to sort a dictionary based on its values rather than its keys.

## 2. Tuples & Slicing
1. **[DONE] Immutable Storage:** Create a tuple representing a fixed coordinate (x, y, z) and try to change one value (observe the error).
2. **[DONE] Tuple Unpacking:** Assign a tuple `(10, 20, 30)` to three variables `a, b, c` in a single line.
3. **[DONE] Basic Slicing:** Take the list `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` and slice it to get `[2, 3, 4, 5]`.
4. **[DONE] Reverse Slicing:** Use a negative step slice `[::-1]` to reverse a string.
5. **[DONE] Step Slicing:** Extract every second element from a list using the `[start:stop:step]` syntax.
6. **[DONE] Last N Elements:** Use slicing to get the last 3 elements of any list, regardless of its length.
7. **[DONE] Tuple Concatenation:** Join two tuples together to create a third tuple.
8. **[DONE] Nested Slicing:** Create a list of lists and use slicing to get the first two sub-lists.
9. **[DONE] Search & Count:** Use `.index()` and `.count()` methods on a tuple of repeated values.
10. **[DONE] The Password Generator:** Write a script that takes a long string of characters and uses random slicing to pick pieces for a password.

## 6. Standard Library (`math`, `random`, `datetime`)
1. **[DONE] Rounding & Power:** Use `math.ceil()`, `math.floor()`, and `math.pow()` to manipulate user input numbers.
2. **[DONE] Constants:** Print the value of `pi` and `e` using the `math` module.
3. **[DONE] Random Choice:** Use `random.choice()` to pick a random name from a list.
4. **[DONE] Shuffling:** Use `random.shuffle()` to reorder a list of tasks in place.
5. **[DONE] Random Ranges:** Generate a random floating-point number between 1.0 and 10.0 using `random.uniform()`.
6. **[DONE] Current Time:** Use `datetime.datetime.now()` to print the current date and time in a readable format.
7. **Date Arithmetic:** Use `timedelta` to find out what the date will be exactly 100 days from today.
8. **Parsing Dates:** Convert a string like "2026-12-25" into a Python `datetime` object.
9. **Formatting Dates:** Print the current date in the format: "Friday, February 28, 2026".
10. **The Birthday Countdown:** Build a script that asks for a birthday and calculates the days, hours, and minutes remaining.

## 7. PEP 8 & Code Style
1. **Naming Audit:** Rename variables like `x`, `temp`, and `data1` in an old script to semantic names.
2. **Import Sorting:** Organize imports into three groups: Standard Library, Third-Party, and Local modules.
3. **Whitespace Control:** Ensure 2 blank lines between functions and 1 blank line between methods in a class.
4. **Line Length:** Break a long string or calculation into multiple lines to stay under 79 characters.
5. **Comment Purpose:** Remove comments that explain "what" code does; replace them with comments explaining "why".
6. **Type Hinting Basics:** Add type hints (`: int`, `: str`) to all variables in a script.
7. **Function Annotations:** Add return type hints (`-> None`, `-> list`) to all functions.
8. **Docstring Implementation:** Write a Google-style docstring for a complex function.
9. **Guard Clauses:** Refactor a nested `if/else` block into "fail-fast" guard clauses.
10. **Style-Guide Audit:** Take your "Flashcard App" and run it against your `style-guide.md` checklist.

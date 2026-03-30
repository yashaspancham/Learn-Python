# Intermediate Mastery Tasks

## 1. Object-Oriented Programming (OOP)
1. **[DONE] Class & Constructor:** Create a `Car` class with `make`, `model`, and `year` attributes set in `__init__`. Print them.
2. **[DONE] Instance Methods:** Add a `description()` method to `Car` that returns a formatted string like "2022 Toyota Corolla".
3. **Class vs Instance Variables:** Add a class variable `total_cars` that increments every time a new `Car` is created.
4. **Encapsulation:** Create a `BankAccount` class with a private `_balance`. Add `deposit()` and `withdraw()` methods that validate input.
5. **Properties:** Use `@property` and `@setter` to expose `_balance` as a controlled attribute with validation.
6. **Inheritance:** Create an `ElectricCar` subclass of `Car` that adds a `battery_range` attribute.
7. **Method Overriding:** Override `description()` in `ElectricCar` to append "| Battery: 300mi" to the output.
8. **`super()`:** Use `super().__init__()` in `ElectricCar` to avoid repeating parent constructor logic.
9. **`__str__` & `__repr__`:** Implement both dunder methods on `BankAccount` — `__str__` for users, `__repr__` for debugging.
10. **Multiple Inheritance:** Create `Flyable` and `Swimmable` mixins, then a `Duck` class that inherits both and calls both methods.
11. **Abstract Classes:** Use `abc.ABC` and `@abstractmethod` to define a `Shape` base class with an abstract `area()` method.
12. **Polymorphism:** Create `Circle` and `Rectangle` subclasses of `Shape`, implement `area()` in each, then call it via a loop.
13. **`__eq__` & `__lt__`:** Add comparison dunder methods to a `Student` class so instances can be compared by GPA.
14. **Dataclasses:** Rewrite the `Student` class using `@dataclass` — observe how `__init__`, `__repr__`, and `__eq__` are auto-generated.
15. **The Library System:** Build a `Library` class containing a list of `Book` objects. Add methods to borrow, return, and search by title. Use inheritance for `EBook`.

## 2. Decorators & Closures
1. **Inner Functions:** Write a function that defines and returns another function. Call the returned function.
2. **Closures:** Write a `make_multiplier(n)` function that returns a closure multiplying any input by `n`.
3. **Basic Decorator:** Write a `@logger` decorator that prints "Calling [function name]" before every function call.
4. **Decorator with Return Value:** Ensure your `@logger` decorator still returns the original function's return value.
5. **`functools.wraps`:** Apply `@functools.wraps` inside your decorator so the wrapped function keeps its original `__name__`.
6. **`@timer` Decorator:** Write a decorator that measures and prints execution time using `time.perf_counter()`.
7. **Decorator with Arguments:** Write a `@repeat(n)` decorator that calls the decorated function `n` times.
8. **Stacking Decorators:** Apply both `@logger` and `@timer` to one function. Observe and explain the execution order.
9. **`@cache` / Memoization:** Use `functools.lru_cache` to memoize a slow recursive Fibonacci function. Compare performance.
10. **Class-Based Decorator:** Implement the `@logger` decorator as a class using `__init__` and `__call__`.
11. **The Performance Monitor:** Write a `@profile(threshold_ms)` decorator that logs a warning only if execution exceeds the threshold.

## 3. Iterators & Generators (`yield`)
1. **Custom Iterator:** Write a `Countdown` class with `__iter__` and `__next__` that counts down from N to 0.
2. **`StopIteration`:** Raise `StopIteration` in `__next__` when the countdown reaches 0. Verify `for` loop stops cleanly.
3. **Basic Generator:** Write a `countdown(n)` generator function using `yield` that does the same as above in far fewer lines.
4. **Infinite Generator:** Write a `integers_from(n)` generator that yields integers starting from `n` forever. Use `itertools.islice` to take the first 10.
5. **Generator Pipeline:** Chain two generators: one that reads lines from a file, and one that filters lines containing a keyword.
6. **`yield from`:** Use `yield from` to flatten a nested list `[[1,2],[3,[4,5]]]` recursively.
7. **Generator Expressions:** Create a generator expression that yields squares of even numbers from 1–100. Sum them without building a list.
8. **`send()` to a Generator:** Write a generator that accumulates values sent to it with `.send()` and yields a running total.
9. **`itertools` Exploration:** Use `itertools.chain`, `itertools.product`, and `itertools.groupby` — one task each showing practical use.
10. **Memory Comparison:** Read a 100MB+ file twice — once with `readlines()` (full load), once with a generator line-by-line. Compare peak RAM using `tracemalloc`.
11. **The Log Analyzer:** Write a generator pipeline that streams a large log file, filters for ERROR lines, and yields parsed dicts `{timestamp, message}`.

## 4. Context Managers (`with` statements)
1. **File Context Manager:** Open and read a file using `with open(...)`. Confirm the file closes automatically by checking `.closed`.
2. **Exception in `with` Block:** Raise an error inside a `with` block. Verify the file is still closed in the `finally` sense.
3. **`contextlib.contextmanager`:** Write a `@contextmanager` called `timer()` that prints elapsed time after the block exits.
4. **`__enter__` & `__exit__`:** Implement a `ManagedFile` class with `__enter__` (open file) and `__exit__` (close file + handle exceptions).
5. **`__exit__` Suppression:** Return `True` from `__exit__` to suppress a specific exception type. Test it.
6. **Nested Context Managers:** Open two files simultaneously using a single `with` statement. Write one's content into the other.
7. **Database Transaction Wrapper:** Simulate a DB connection with a context manager that commits on clean exit and rolls back on exception.
8. **`contextlib.suppress`:** Use `contextlib.suppress(FileNotFoundError)` to safely attempt reading a file that may not exist.
9. **Reentrant Context Manager:** Use `contextlib.RLock()` as a context manager inside nested calls. Observe it doesn't deadlock.
10. **The Secure DB Wrapper:** Build a `Transaction` context manager for a SQLite connection — commits on success, rolls back and logs on any exception.

## 5. Advanced Exception Handling
1. **Custom Exception:** Define a `ValidationError(ValueError)` subclass with a custom message and an extra `field` attribute.
2. **Exception Hierarchy:** Create `AppError` as a base, then `NetworkError` and `DatabaseError` as subclasses. Catch them at different levels.
3. **`raise from`:** Re-raise a low-level `OSError` as a `DatabaseError` using `raise DatabaseError(...) from original_error`. Inspect `__cause__`.
4. **`try/except/else/finally`:** Write a function that uses all four clauses — explain in a comment when each block runs.
5. **Multiple `except` Clauses:** Handle `KeyError`, `TypeError`, and a catch-all `Exception` separately in one `try` block.
6. **Exception Groups (Python 3.11+):** Raise an `ExceptionGroup` with multiple errors and handle them with `except*`.
7. **Retry Logic:** Write a `@retry(times, delay)` decorator that retries a failing function N times with a sleep between attempts.
8. **Context-Aware Errors:** Log the full traceback to a file using `traceback.format_exc()` when an exception is caught.
9. **`warnings` Module:** Use `warnings.warn()` to emit a `DeprecationWarning` when a legacy function is called.
10. **The Robust CLI Tool:** Build a CLI script that defines custom error types and handles missing config, bad input, and network failures each with a distinct message and exit code.

## 6. Modules & Virtual Environments
1. **Create a Module:** Split a multi-function script into a module file and a `main.py` that imports from it.
2. **`__init__.py`:** Create a package folder with `__init__.py` that exposes only selected functions via `__all__`.
3. **Relative vs Absolute Imports:** Use both relative (`from .utils import`) and absolute imports in a package. Note when each is appropriate.
4. **`if __name__ == "__main__"`:** Add a guard to a module so its test code only runs when executed directly, not when imported.
5. **`sys.path` Manipulation:** Append a directory to `sys.path` at runtime and import a module from a non-standard location.
6. **Virtual Environment:** Create a `venv`, install `requests`, freeze to `requirements.txt`, then recreate from it in a fresh `venv`.
7. **`importlib`:** Use `importlib.import_module()` to dynamically import a module by name given as a string variable.
8. **Inspect a Module:** Use `dir()` and `help()` to explore an unfamiliar stdlib module (e.g., `collections`).
9. **`__all__`:** Define `__all__` in a module and verify that `from module import *` only imports listed names.
10. **The Packageable API Client:** Build a `weather/` package with `__init__.py`, `client.py` (fetches data), and `models.py` (parses response). Make it importable and runnable as a script.

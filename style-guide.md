# Python Style Guide for LLMs & Humans

To ensure maximum compatibility with AI code analysis and long-term human maintainability, follow these standards.

## 1. Naming Conventions (Semantic & Explicit)
- **Variables/Functions:** `snake_case`. Be descriptive: `is_user_authenticated` is better than `auth`.
- **Classes:** `PascalCase`. Use nouns: `DataPipeline`.
- **Constants:** `UPPER_SNAKE_CASE`.
- **Private Members:** Prefix with a single underscore `_internal_method`.

## 2. Type Hinting (Mandatory)
Always use Python's `typing` module. This helps LLMs understand data flow instantly.
```python
def process_data(data: list[int], threshold: float) -> dict[str, bool]:
    ...
```

## 3. Documentation (Google Style)
Use triple-quote docstrings for all modules, classes, and functions.
```python
def calculate_total(price: float, tax: float) -> float:
    """Calculates the final price including tax.

    Args:
        price: The base cost of the item.
        tax: The tax percentage (0.0 to 1.0).

    Returns:
        The total price after tax.
    """
```

## 4. Structure & Logic
- **Brevity:** Keep functions under 20 lines. If it's longer, refactor.
- **Fail Fast:** Use guard clauses to handle errors early.
- **Pure Functions:** Prefer functions that don't modify global state.
- **PEP 8:** Strict adherence to whitespace, imports (standard lib first, then third-party), and line length (79-88 chars).

## 5. LLM-Specific Tips
- **Self-Documenting Code:** If you need a comment to explain *what* the code does, the code isn't clear enough. Use comments to explain *why* (the intent).
- **Consistent Returns:** Ensure a function always returns the same type.
- **Avoid "Magic":** Don't use `getattr`, `setattr`, or `globals()` unless absolutely necessary; they confuse static analysis.

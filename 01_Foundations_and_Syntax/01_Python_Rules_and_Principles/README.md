# Python Rules & Principles

Before writing logic, it is essential to understand the governing rules and philosophy of Python. Python emphasizes code readability and simplicity, guided by a set of principles known as The Zen of Python (which you can read by typing import this in your terminal).

## Main Principles

**Readability counts:** Code is read much more often than it is written.

**Explicit is better than implicit:** Avoid "magic" behaviors; make the code's intent obvious.

**Indentation is syntax:** Unlike C++ or Java which use curly braces {}, Python uses whitespace (standard is 4 spaces) to define code blocks.

## Naming Rules (PEP 8 Standards)

Variables and functions must use snake_case (e.g., user_age, calculate_total()).

Classes use PascalCase (e.g., UserProfile, LogicGate).

Constants use UPPER_SNAKE_CASE (e.g., MAX_CONNECTIONS = 100).

**Hard Rules:** Names can contain letters, numbers, and underscores, but cannot start with a number. They are case-sensitive (Age and age are different).

## Reserved Words

Python has built-in keywords that cannot be used as variable names. Attempting to do so will cause a SyntaxError.

**Examples:** True, False, None, if, else, for, while, def, class, import, return.

**Note:** You can view all current keywords by running:

```python
import keyword; 
print(keyword.kwlist))
```

## Comments & Documentation

Comments explain why code does something, not what it does.

```Python

# This is a single-line comment

"""
This is a multi-line string.
When placed at the top of a function or file,
it acts as a 'Docstring' to document the code's purpose.
"""
```

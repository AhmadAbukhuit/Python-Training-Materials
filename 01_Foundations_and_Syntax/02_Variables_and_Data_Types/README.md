# Variables & Data Types: The Memory Foundations of Python

**What is a variable?**
In Python, a variable is not a "box" that stores data. Instead, it is a label or a reference tag attached to an object in memory.

Python is dynamically typed, meaning you do not need to declare a variable's type explicitly before using it. The Python interpreter infers the type at runtime based on the value assigned.

**Example:**
When you type x = 10, Python does three things:

1. Creates an integer object with the value 10 in a private memory space called the Heap.
2. Assigns a unique memory address to that object.
3. Binds the label x to that memory address.

If you then type y = x, Python does not copy the number 10. It simply attaches the label y to the exact same memory address as x. You can verify this using the id() function, which returns an object's memory address.

However, Python is also strongly typed. It will not automatically coerce types in ways that lose data (e.g., it won't silently add a string to an integer without explicit conversion).

## Data Types Overview

Python is dynamically typed; the interpreter infers the type at runtime.

* **Integers (int):** Whole numbers of arbitrary length.
* **Floats (float):** Decimal numbers (IEEE 754 double precision).
* **Strings (str):** Immutable sequences of Unicode characters.
* **Booleans (bool):** Represents truth values (True or False).
  
Example: Defining System States

```python
# Variables representing data from a PV Solar Power Plant inspection
panel_id = "Zone_A_String_14"   # str: Alphanumeric identifier
surface_temp_celsius = 48.5     # float: Continuous decimal measurement
defect_detected = False         # bool: Binary state
packet_transmit_rate = 1024     # int: Discrete count

# Checking types dynamically
print(type(surface_temp_celsius)) # Output: <class 'float'>
```

**Type Casting:**

Often, you must convert data from one type to another, especially when reading from files or taking user input.

```python
string_temp = "48.5"
actual_temp = float(string_temp) # Casts the string to a usable float
```

## Strings and String Operations

Strings (`str`) are ordered sequences of Unicode characters enclosed in single (`'...'`), double (`"..."`), or triple quotes (`'''...'''`).

**Key Concept: Immutability**  
Strings in Python are **immutable**. Once created in memory, they cannot be modified in place. Any method that appears to modify a string actually creates and returns a brand-new string.

```python
sample = "Python"
# sample[0] = "J"  <-- TypeError: 'str' object does not support item assignment
```

### 1. Combining and Repeating Strings

You can use standard math operators to combine or duplicate strings:

```python
# Concatenation (+) joins strings together
greeting = "Hello" + " " + "World"
print(greeting)  # "Hello World"

# Repetition (*) duplicates a string multiple times
divider = "-" * 30
print(divider)   # "------------------------------"
```

---

### 2. String Indexing and Slicing `[start:stop:step]`

Strings are indexed starting from `0`. You can also use negative indices to count backward from the end:

```text
 Forward Index:    0   1   2   3   4   5
 Character:        P   y   t   h   o   n
 Reverse Index:   -6  -5  -4  -3  -2  -1
```

Use slicing syntax `string[start:stop:step]` to extract portions of text:

```python
text = "Python Programming"

# Indexing (single character)
print(text[0])       # "P" (first character)
print(text[-1])      # "g" (last character)

# Slicing: [start:stop] (stop is exclusive)
print(text[0:6])     # "Python"
print(text[:6])      # "Python" (omitting start defaults to index 0)
print(text[7:])      # "Programming" (omitting stop goes to the end)

# Stepping: [start:stop:step]
print(text[::2])     # "Pto rgamn" (every 2nd character)
print(text[::-1])    # "gnimmargorP nohtyP" (reverses the string!)
```

---

### 3. Essential String Manipulation Methods

String methods can be categorized by their real-world use:

#### A. Trimming Whitespace (Data Cleaning)

* `.strip()`: Removes leading and trailing whitespace.
* `.lstrip()` / `.rstrip()`: Removes whitespace only from the left or right.

```python
raw_input = "   admin_user   \n"
print(raw_input.strip())  # "admin_user"
```

#### B. Changing Letter Casing

* `.upper()`: Converts all characters to uppercase.
* `.lower()`: Converts all characters to lowercase.
* `.title()`: Capitalizes the first letter of each word.

```python
name = "ahmad abu khuit"
print(name.upper())  # "AHMAD ABU KHUIT"
print(name.title())  # "Ahmad Abu Khuit"
```

#### C. Searching and Replacing

* `.replace(old, new)`: Replaces occurrences of a substring with another.

```python
path = "C:/users/documents/data.csv"
linux_path = path.replace("/", "\\")
print(linux_path)  # "C:\users\documents\data.csv"
```

#### D. Splitting and Joining

* `.split(separator)`: Splits a string into a list of substrings.
* `separator.join(iterable)`: Glues a list of strings together into one string.

```python
# Splitting CSV data into a list
csv_row = "sensor_1,48.5,active"
fields = csv_row.split(",")
print(fields)  # ['sensor_1', '48.5', 'active']

# Joining a list back into a formatted string
joined = " | ".join(fields)
print(joined)  # "sensor_1 | 48.5 | active"
```

#### E. Text Alignment

* `.center()`: Centers the text, padding both sides equally, `text.center(width, fillchar=' ')`.
* `.ljust()`: Left-aligns the text, padding on the right, `text.ljust(width, fillchar=' ')`.
* `.rjust()`: Right-aligns the text, padding on the left, `text.rjust(width, fillchar=' ')`.

    **How `.center()` Calculates Padding:**

    ```text
    "STATUS".center(14, "=")

    Total Width = 14 characters
    Text Length = 6 characters  ("STATUS")
    Remaining   = 8 spaces (4 on left, 4 on right)

    Result:  ====STATUS====
    ```

    **Code Example: Building a Clean Terminal Menu**

    ```python
    # Centering headers with custom fill characters
    header = "SYSTEM DASHBOARD".center(36, "=")
    print(header)

    # Aligning columns using ljust and rjust
    print("Component".ljust(20) + "Status".rjust(16))
    print("-" * 36)
    print("Solar Inverter 01".ljust(20) + "ONLINE".rjust(16))
    print("Battery Bank B".ljust(20) + "CHARGING".rjust(16))
    print("Grid Relay".ljust(20) + "STANDBY".rjust(16))
    print("=" * 36)
    ```

    **Output:**

    ```text
    ========SYSTEM DASHBOARD========
    Component                    Status
    ------------------------------------
    Solar Inverter 01            ONLINE
    Battery Bank B             CHARGING
    Grid Relay                  STANDBY
    ====================================
    ```

---

### 4. Built-in String Validation Methods

Python has powerful built-in validation methods designed to inspect the contents of a string before processing, sanitizing, or type-casting it. All validation methods return a Boolean (`True` or `False`).

#### 1. `.isalpha()` (Alphabetic Characters Only)

Returns `True` if **all** characters in the string are letters (a-z, A-Z) and the string is not empty. Returns `False` if there are numbers, spaces, or punctuation.

```python
"Python".isalpha()      # True
"Python 3".isalpha()    # False (contains a space and digit)
"User@1".isalpha()      # False (contains symbol and digit)
```

#### 2. `.isalnum()` (Alphanumeric Characters)

Returns `True` if **all** characters are either letters or numbers and the string is not empty. Useful for checking usernames, IDs, and serial numbers.

```python
"Admin123".isalnum()    # True
"Zone_A".isalnum()      # False (underscore '_' is a punctuation symbol)
"Order#45".isalnum()    # False (contains '#')
```

#### 3. `.isdecimal()`, `.isdigit()`, `.isnumeric()` (Numeric Digits)

These methods verify whether the string contains numeric characters:

* **`.isdecimal()`**: Strict check for base-10 digits (`0`–`9`). Best for validating integers before calling `int()`.
* **`.isdigit()`**: Checks for digits, including special numeric characters like superscripts (`²`).
* **`.isnumeric()`**: Broadest check; includes digits, superscripts, fractions (`½`), and Roman numeral characters in Unicode.

```python
"1024".isdecimal()      # True
"1024".isdigit()        # True
"1024".isnumeric()      # True

"2²".isdecimal()        # False
"2²".isdigit()          # True
"½".isnumeric()         # True
```

> [!WARNING]
> **Validation Gotcha:** Numeric validation methods return `False` for negative signs (`"-42"`) and decimal points (`"3.14"`), because `"-"` and `"."` are punctuation characters, not digits.

#### 4. `.isspace()` (Whitespace Only)

Returns `True` if the string contains only whitespace characters (spaces, tabs `\t`, newlines `\n`, carriage returns `\r`) and has at least one character.

```python
"   \t\n  ".isspace()    # True
"".isspace()            # False (empty string)
"  hello  ".isspace()    # False (contains letters)
```

#### 5. `.islower()` and `.isupper()` (Letter Casing)

* **`.islower()`**: Returns `True` if all cased characters are lowercase.
* **`.isupper()`**: Returns `True` if all cased characters are uppercase.

*(Numbers and symbols are ignored as long as at least one cased letter is present).*

```python
"hello world".islower() # True
"HELLO 123!".isupper()  # True (digits and punctuation are ignored)
"123".isupper()         # False (no cased characters)
```

#### 6. `.istitle()` (Title Case)

Returns `True` if every word begins with an uppercase letter followed by lowercase letters.

```python
"Python Training Materials".istitle()  # True
"Python training materials".istitle()  # False
```

#### 7. `.isidentifier()` (Valid Python Variable Name)

Returns `True` if the string is a valid variable or function identifier according to Python's syntax rules (cannot start with a digit, no spaces or hyphens, only letters, numbers, and underscores).

```python
"user_score".isidentifier()   # True
"_internal_id".isidentifier() # True
"2nd_attempt".isidentifier()  # False (starts with a digit)
"user-name".isidentifier()    # False (contains hyphen '-')
```

#### 8. `.isascii()` (ASCII Character Range)

Returns `True` if all characters fall within the standard ASCII range (code points 0–127). Returns `True` for an empty string.

```python
"hello".isascii()        # True
"café".isascii()         # False ('é' is non-ASCII Unicode)
```

---

### String Validation Reference Summary

| Method | Returns `True` When All Characters Are: | Rejects (Returns `False`): | Common Use Case |
| :--- | :--- | :--- | :--- |
| **`.isalpha()`** | Letters only (`A-Z`, `a-z`, Unicode letters) | Numbers, spaces, symbols | Validating names, country codes |
| **`.isalnum()`** | Letters and digits | Spaces, punctuation (`_`, `-`, `#`) | Usernames, serial numbers, license keys |
| **`.isdecimal()`** | Base-10 digits (`0-9`) | Negative signs, decimals, letters | Safe integer conversion via `int()` |
| **`.isspace()`** | Whitespace (` `, `\t`, `\n`) | Any non-whitespace character | Detecting blank or empty-looking inputs |
| **`.isupper()`** | Uppercase letters | Any lowercase letter | Checking acronyms, constants |
| **`.islower()`** | Lowercase letters | Any uppercase letter | Normalizing lowercase slugs or emails |
| **`.istitle()`** | Title-cased words | Irregular capitalization | Validating capitalized book/page titles |
| **`.isidentifier()`** | Valid Python identifier syntax | Leading digits, hyphens, spaces | Dynamic attribute creation, code generators |
| **`.isascii()`** | ASCII characters (0–127) | Emojis, accented letters (`é`, `ñ`, `ü`) | Ensuring legacy system compatibility |

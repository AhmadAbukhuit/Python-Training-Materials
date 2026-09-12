# Dictionaries: Key-Value Mapping

If a list is like a line of boxes where each box has a number (its index), a dictionary is like a filing cabinet where every folder has a custom label.

Lists are terrible for storing structured records like a user profile. If you have a list `["Alice", 28, "Engineer"]`, you have to memorize that index `1` is the age. **Dictionaries** solve this by using **Key-Value pairs**, allowing you to look up data by its logical name.

## Dictionary Syntax

Dictionaries are created using curly braces `{}`. Every item inside the dictionary consists of a key and a value, separated by a colon `:`.

```python
# Creating a dictionary to represent a user profile
user = {
    "username": "coder_alice",
    "age": 28,
    "role": "Engineer",
    "is_active": True
}
```

* **Keys:** Must be immutable data types (like strings, integers, or tuples) and must be unique.
* **Values:** Can be absolutely anything—strings, integers, booleans, lists, or even other dictionaries.

## Accessing Data

There are two ways to retrieve data from a dictionary.

### Bracket Notation (The Strict Way)

You pass the key inside square brackets. If the key exists, it returns the value. If the key does not exist, it crashes your program with a `KeyError`.

```python
print(user["username"])  # Outputs: coder_alice
# print(user["email"])   <-- Crashes with KeyError
```

### The `.get()` Method (The Safe Way)

Professional developers prefer `.get()`. If the key doesn't exist, it gracefully returns `None` instead of crashing. You can even provide a default fallback value.

```python
print(user.get("age"))           # Outputs: 28
print(user.get("email"))         # Outputs: None
print(user.get("email", "N/A"))  # Outputs: N/A (because the key is missing)
```

## Modifying and Adding Data

Dictionaries are mutable. You add new data and update existing data using the exact same bracket syntax.

```python
# Updating an existing key
user["age"] = 29

# Adding a completely new key-value pair
user["email"] = "alice@example.com"

# Removing a key-value pair
del user["is_active"]
```

## Iterating Through Dictionaries

Because dictionaries are made of pairs, looping through them requires a special method called `.items()`, which unpacks both the key and the value at the same time.

```python
for key, value in user.items():
    print(f"The user's {key} is {value}")
    
# Output:
# The user's username is coder_alice
# The user's age is 29
# The user's role is Engineer
# The user's email is alice@example.com
```

(You can also use `.keys()` if you only need the keys, or `.values()` if you only need the values).

## Nested Dictionaries (The API Precursor)

Dictionaries shine when they hold complex, multi-layered data. A dictionary can hold another dictionary, which perfectly mirrors the structure of **JSON** (the standard format used by APIs across the web).

```python
server_response = {
    "status": "success",
    "data": {
        "user_id": 105,
        "metrics": {
            "logins": 42,
            "uptime_hours": 120.5
        }
    }
}

# Chaining brackets to access deeply nested data
print(server_response["data"]["metrics"]["logins"])  # Outputs: 42
```

Mastering nested dictionaries here will make Module 07 (FastAPI) much easier!

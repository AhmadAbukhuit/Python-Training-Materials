# File Input/Output (I/O)

Everything we have done so far happens in your computer's RAM (Random Access Memory). When your Python script finishes running, all your lists, dictionaries, and variables vanish instantly.

To make data persist, whether it is saving user preferences, logging errors, or exporting a data report, you need to write it to your hard drive. This is known as File Input/Output (I/O).

## The Golden Rule: Context Managers

In older programming languages, interacting with a file took three steps: open the file, write the data, and close the file. If your program crashed before reaching the "close" step, the file could become locked or permanently corrupted.

Python solves this elegantly using a Context Manager, denoted by the `with` keyword.

When you open a file using `with`, Python creates a secure temporary context. The moment your code finishes (or even if it crashes), Python automatically and safely closes the file for you. You should never use the raw `open()` function without a `with` statement.

## Reading and Writing Text Files

To interact with a file, we use the built-in `open()` function. It requires two main arguments: the file path, and the mode (`'r'` for read, `'w'` for write, `'a'` for append).

Writing to a File (`'w'`)\
**⚠️ Warning:** The `'w'` mode will completely overwrite the file if it already exists!

```python
# Create a new file (or overwrite an existing one)
with open("user_log.txt", "w") as file:
    file.write("User Alice logged in at 10:00 AM.\n")
    file.write("User Bob logged in at 10:05 AM.\n")
```

**Appending to a File (`'a'`)**\
If you want to add new data to the bottom of an existing file without erasing the old data, use append mode.

```python
with open("user_log.txt", "a") as file:
    file.write("User Charlie logged in at 10:15 AM.\n")
```

**Reading a File (`'r'`)**

```python
# 'r' is the default mode, but it is best practice to be explicit
with open("user_log.txt", "r") as file:
    # Read the entire file contents into a single string
    content = file.read()
    print(content)
```

(Pro-tip: If dealing with massive files, you can read them line-by-line using `for line in file:` to save memory).

## Handling JSON Data

Plain text is great for logs, but terrible for structured data. If you write a dictionary to a text file, it just becomes a giant string. When you read it back, you can't easily extract the keys or values.

To save structured data, we use JSON (JavaScript Object Notation). It is the universal language of the web. Python comes with a built-in `JSON` module that flawlessly translates Python Dictionaries into JSON files, and vice versa.

**Saving a Dictionary to a JSON File (`json.dump`)**

```python
import json

user_profile = {
    "username": "coder_alice",
    "role": "Engineer",
    "languages": ["Python", "Go", "JavaScript"]
}

# Notice we use 'w' mode because we are writing
with open("profile.json", "w") as file:
    # dump() takes two arguments: the data, and the file object
    json.dump(user_profile, file, indent=4) 
    
# The indent=4 argument formats the file so it is easy for humans to read!
```

**Loading a JSON File into a Dictionary (`json.load`)**

```python
import json

with open("profile.json", "r") as file:
    # load() reads the file and reconstructs the Python dictionary
    loaded_data = json.load(file)

# Now we can interact with it exactly like a normal dictionary!
print(f"Welcome back, {loaded_data['username']}!")
print(f"Your primary language is {loaded_data['languages'][0]}.")
```

Mastering the `JSON` module is critical. In Module 07 (FastAPI), practically every piece of data you send or receive across the internet will be formatted as JSON!

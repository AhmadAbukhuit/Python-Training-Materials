# Data Comprehensions: The Pythonic Way

As you spend more time in the Python ecosystem, you will hear the word "Pythonic." This refers to code that doesn't just work, but utilizes Python's unique features to be as clean, readable, and efficient as possible.

The ultimate example of Pythonic code is the Comprehension. Comprehensions allow you to create, filter, and modify collections (Lists, Dictionaries, and Sets) in a single, highly optimized line of code.

## List Comprehensions

Let's say you have a list of prices, and you want to apply a 10% tax to each one to create a new list.

### The Traditional Way (Standard for loop)

```python
prices = [10.0, 20.0, 50.0]
taxed_prices = []

for price in prices:
    taxed_prices.append(price * 1.1)
```

### The Pythonic Way (List Comprehension)

```python
prices = [10.0, 20.0, 50.0]
taxed_prices = [price * 1.1 for price in prices]
```

Notice how the loop and the `append()` action are compressed into a single, highly readable sentence directly inside the square brackets.

### Adding Filters (The if clause)

Comprehensions can also filter data on the fly. Let's create a list of only the even numbers from 1 to 10:

```python
# Syntax: [expression for item in iterable if condition]
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)  # Outputs: [2, 4, 6, 8, 10]
```

## Dictionary Comprehensions

You can apply this exact same logic to build dictionaries dynamically. Instead of square brackets, we use curly braces `{}` and specify both the `key: value`.

Imagine you have a list of usernames, and you want to create a dictionary mapping each name to the length of the name:

```python
names = ["Alice", "Bob", "Charlie"]

# Syntax: {key_expression: value_expression for item in iterable}
name_lengths = {name: len(name) for name in names}

print(name_lengths)
# Outputs: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

## Set Comprehensions

Set comprehensions use the same curly braces `{}` as dictionaries, but without the colon (`:`). They automatically remove duplicates while applying your logic.

Suppose you have a list of words with messy capitalization, and you want a clean set of unique lowercase words:

```python
words = ["Apple", "banana", "APPLE", "Orange", "Banana"]

unique_lowercase = {word.lower() for word in words}

print(unique_lowercase)
# Outputs: {'orange', 'apple', 'banana'}
```

## The Golden Rule of Comprehensions

Comprehensions are actually evaluated at the C-language level under the hood, making them incredibly fast. However, readability always comes first.

While you can write nested comprehensions (a loop inside a loop inside a comprehension), you shouldn't. If your comprehension wraps across three lines and takes a minute to understand, it is no longer Pythonic. Break it back down into a standard `for` loop.

**Rule of Thumb:** Use comprehensions for simple mapping (modifying items) and filtering (removing items). If the logic requires `elif` statements or complex data transformations, use a standard loop.

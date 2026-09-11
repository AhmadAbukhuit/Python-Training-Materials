# Lists & Tuples: Sequential Data

When you need to store 100 usernames, creating 100 separate variables (`user1`, `user2`, etc.) is impossible to manage. Instead, we use collections to group related data together.

The two most fundamental collections in Python for ordered, sequential data are Lists and Tuples.

## Python Lists (The Mutable Workhorse)

A list is an ordered collection of items. In Python, lists are created using square brackets `[]`.

Lists are mutable, meaning their contents can be changed, added to, or removed after the list is created. They can also hold mixed data types, though it is best practice to keep them uniform.

```python
# Creating a list of temperatures
temperatures = [72.5, 74.1, 71.8, 75.0]

# 1. Accessing elements (0-based indexing)
print(temperatures[0])  # Outputs: 72.5

# 2. Modifying an element (Mutating)
temperatures[1] = 79.9

# 3. Adding elements
temperatures.append(80.2)       # Adds to the end of the list
temperatures.insert(0, 68.5)    # Inserts 68.5 at index 0

# 4. Removing elements
temperatures.remove(71.8)       # Removes the specific value
last_temp = temperatures.pop()  # Removes and returns the very last item
```

## The Power of Slicing

Python has a brilliant feature for extracting smaller sections of a list called slicing. The syntax is `list[start:stop:step]`.

* `start`: The index where the slice begins (inclusive).
* `stop`: The index where the slice ends (exclusive).
* `step`: How many items to jump (optional).

```python
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Get the first three items (index 0, 1, 2)
print(alphabet[0:3])    # ['A', 'B', 'C']

# If you leave out the start, it assumes 0
print(alphabet[:3])     # ['A', 'B', 'C']

# Negative indexing counts from the end of the list
print(alphabet[-1])     # ['G'] (The last item)
print(alphabet[-3:])    # ['E', 'F', 'G'] (The last three items)

# Stepping (every other item)
print(alphabet[0:7:2])  # ['A', 'C', 'E', 'G']
```

## Tuples (The Immutable Vault)

A tuple is also an ordered collection, but it is created using parentheses `()`.

The critical difference is that tuples are immutable. Once a tuple is created, its size and contents can never be changed. You cannot append to it, remove from it, or reassign its elements.

```python
# Creating a tuple representing database connection credentials
db_config = ("localhost", 5432, "admin_user")

print(db_config[0]) # Outputs: "localhost"

# Attempting to mutate a tuple will crash your program:
# db_config[1] = 8080  <-- TypeError: 'tuple' object does not support item assignment
```

**Why use Tuples if Lists do more?**

1. **Safety:** If you pass a tuple into a function, you are mathematically guaranteed that the function cannot accidentally alter your data.
2. **Performance:** Because Python knows a tuple will never change size, it optimizes them in memory. Tuples are slightly faster and use less memory than lists.
3. **Dictionary Keys:** As you will see in the next topic, you can use a tuple as a key in a dictionary, but you cannot use a list.

## Comparison Summary

| Feature | List `[]` | Tuple `()` |
| ------- | --------- | ---------- |
| Mutability | Mutable (can change) | Immutable (locked) |
| Methods | Many (`append`, `remove`, `sort`) | Few (`count`, `index`) |
| Best Used For | Dynamic data (user inputs, queues) | Fixed data (coordinates, settings) |
| Memory | Heavier | Lighter |

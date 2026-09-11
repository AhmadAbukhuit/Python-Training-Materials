# Module 04: Data Structures & I/O

Welcome to Module 04. Up until now, we have mostly worked with single variables—a single string, an integer, or a boolean. But in the real world, data comes in massive, complex collections: user profiles, product catalogs, sensor logs, and financial records.

In this module, you will learn how to store, manipulate, and retrieve complex data using Python's powerful built-in data structures. You will also learn how to bridge the gap between temporary computer memory and permanent storage by reading from and writing to files on your hard drive.

## Topics Covered

* **[1. Lists & Tuples: Sequential Data](./01_Lists_and_Tuples/)**
  Understanding ordered collections, the critical difference between mutable and immutable data, slicing, and list methods.
* **[2. Dictionaries: Key-Value Mapping](./02_Dictionaries/)**
  Building scalable relationships using key-value pairs, managing nested data structures, and performing lightning-fast lookups.
* **[3. Sets: Unique Collections](./03_Sets/)**
  Managing collections of unique items, deduplication, and utilizing mathematical set operations (union, intersection, difference).
* **[4. Data Comprehensions: The Pythonic Way](./04_Data_Comprehensions/)**
  Writing elegant, highly optimized one-liners to dynamically generate lists, dictionaries, and sets without standard loops.
* **[5. The `collections` Module: Advanced Structures](./05_Collections_Module/)**
  Leveling up with specialized data structures like `defaultdict`, `Counter`, `deque`, and `namedtuple` for professional, high-performance tasks.
* **[6. File Input/Output (I/O):](./06_File_IO/)**
  Persisting data safely using Context Managers (the `with` statement), and parsing both standard text files and structured JSON data.

---

## Hands-On Practice Tasks

### Task 4.1: The Inventory Manager (Sets & Lists)

**Objective:** Use Sets to clean up messy data and Lists to return it in a structured format.

* **Where to work:** Navigate to the **[task_4_1_inventory](./Tasks/task_4_1_inventory/)** directory.
* **Requirements:**
    * Create a file named `inventory.py`.
    * Write a function called `get_unique_items(item_list)`.
    * The function should take a list of strings (which may contain duplicates), convert it to a set to remove the duplicates, and then return a sorted list of the unique items.
* **Execution:** Run the automated test script to verify your function handles the data correctly.

**How to test your code:**

```bash
cd task_4_1_inventory
python test_inventory.py
```

---

### Task 4.2: The Safe Directory (Dictionaries)

**Objective:** Practice safely retrieving and updating nested dictionary data without crashing the program.

* **Where to work:** Navigate to the **[task_4_2_directory](./Tasks/task_4_2_directory/)** directory.
* **Requirements:**
    * Create a file named `directory.py`.
    * Write a function called `get_salary(employee_dict, emp_id)`. It should use the `.get()` method to safely return the employee's salary. If the `emp_id` does not exist, return the string `"Not Found"`.
    * Write a second function called `update_salary(employee_dict, emp_id, new_salary)`. It should update the dictionary in place.
* **Execution:** Run the test script.

**How to test your code:**

```bash
cd task_4_2_directory
python test_directory.py
```

---

### Task 4.3: The Data Optimizer (Comprehensions & Counter)

**Objective:** Replace standard loops with high-performance Pythonic tools.

* **Where to work:** Navigate to the **[task_4_3_optimizer](./Tasks/task_4_3_optimizer/)** directory.
* **Requirements:**
    * Create a file named `optimizer.py`.
    * Write a function called `filter_evens(numbers)` that takes a list of integers and returns a new list of only the even numbers using a List Comprehension (do not use a standard `for` loop).
    * Write a function called `get_top_word(word_list)` that imports and uses `Counter` from the `collections` module to return the single most common word in the list.
* **Execution:** Run the test script.

**How to test your code:**

```bash
cd task_4_3_optimizer
python test_optimizer.py
```

---

### Task 4.4: The Save State (JSON File I/O)

**Objective:** Persist Python dictionaries to the hard drive as JSON, and load them back into memory.

* **Where to work:** Navigate to the **[task_4_4_save_state](./Tasks/task_4_4_save_state/)** directory.
* **Requirements:**
    * Create a file named `save_state.py`.
    * Import the built-in `json` module.
    * Write a function called `save_data(data_dict, filename)`. It should use a `with` statement to open the file in write (`"w"`) mode and use `json.dump()` to save the dictionary.
    * Write a function called `load_data(filename)`. It should use a `with` statement to open the file in read (`"r"`) mode and use `json.load()` to return the dictionary.
* **Execution:** Run the test script. It will use your functions to write a temporary file to your hard drive and read it back.

**How to test your code:**

```bash
cd task_4_4_save_state
python test_save_state.py
```

---

## Mini Projects

### The Server Log Analyzer

**Scenario:** You have just been handed a messy server access log file from the company's main web server. The security team needs a structured JSON report detailing unique visitors, endpoint traffic, and a list of failed requests (potential attacks).

Your job is to combine everything you've learned about File I/O, Sets, Comprehensions, and the `collections` module to process this text file efficiently.

#### 📁 The Input Data

Navigate to the **[Projects](./Projects/)** directory in this repository. Inside, you will find a pre-made file named `server_logs.txt` containing the messy data you need to process.

For reference, the file contains the following simulated logs:

```text
[2026-09-11 10:00:01] 192.168.1.50 /login 200
[2026-09-11 10:00:05] 10.0.0.12 /dashboard 200
[2026-09-11 10:01:14] 192.168.1.50 /api/data 500
[2026-09-11 10:02:00] 172.16.0.5 /login 401
[2026-09-11 10:02:15] 10.0.0.12 /dashboard 200
[2026-09-11 10:05:30] 192.168.1.50 /login 200
[2026-09-11 10:06:01] 172.16.0.5 /admin 403
[2026-09-11 10:08:22] 10.0.0.12 /api/data 200
```

#### 🛠️ Project Requirements

Create a file named `log_analyzer.py` and write a script that completes the following steps:

**Step 1: Parse with `namedtuple`**

Import `namedtuple` from the `collections` module. Create a named tuple called `LogEntry` with four fields: `timestamp`, `ip_address`, `endpoint`, and `status_code`.

**Step 2: Read the File (File I/O)**

Using a Context Manager (`with open...`), read the `server_logs.txt` file line by line. Parse each line, create a `LogEntry` object for it, and append it to a master list called `logs`. *(Hint: The `.split()` method will be very helpful here)*.

**Step 3: Extract Unique IPs (Sets)**

Create a function or use a Set Comprehension to extract a collection of all unique IP addresses that accessed the server. Convert this set into a standard list.

**Step 4: Endpoint Popularity (`Counter`)**

Import `Counter` from the `collections` module. Use it to determine exactly how many times each endpoint (`/login`, `/dashboard`, etc.) was accessed.

**Step 5: Identify Failed Requests (Comprehensions)**

Using a List Comprehension, create a list of dictionaries for all logs where the `status_code` is not `200`. Each dictionary should look like this: `{"ip": "172.16.0.5", "endpoint": "/admin", "status": "403"}`.

**Step 6: Export the Report (JSON)**

Combine your findings into a single, structured Python dictionary called `security_report`:

```python
security_report = {
    "total_requests": 8,
    "unique_ips": [...],       # From Step 3
    "endpoint_counts": {...},  # From Step 4 (Convert Counter to a dict)
    "failed_requests": [...]   # From Step 5
}
```

Finally, use the `json` module and a Context Manager to save this dictionary to your hard drive as a file named `security_report.json`. Ensure you use `indent=4` so it is easily readable by the security team!

#### ✅ Expected Output

If your script runs correctly, you should see a new file called `security_report.json` appear in your directory with these exact contents:

```JSON
{
    "total_requests": 8,
    "unique_ips": [
        "10.0.0.12",
        "192.168.1.50",
        "172.16.0.5"
    ],
    "endpoint_counts": {
        "/login": 3,
        "/dashboard": 2,
        "/api/data": 2,
        "/admin": 1
    },
    "failed_requests": [
        {
            "ip": "192.168.1.50",
            "endpoint": "/api/data",
            "status": "500"
        },
        {
            "ip": "172.16.0.5",
            "endpoint": "/login",
            "status": "401"
        },
        {
            "ip": "172.16.0.5",
            "endpoint": "/admin",
            "status": "403"
        }
    ]
}
```

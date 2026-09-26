# Module 01: Foundations & Syntax

Welcome to the first module of the Python Training Program. This section covers the fundamental building blocks of Python programming, transitioning from basic variable assignment to complex logical iterations.

## Topics Covered

* **[01. Python Rules & Principles:](./01_Python_Rules_and_Principles/)**  
  Understanding the governing rules, PEP 8 style guide, and philosophy of Python.

* **[02. Variables & Data Types:](./02_Variables_and_Data_Types/)**  
  Understanding primitive data types including Integers, Floats, Strings, and Booleans.

* **[03. Operators:](./03_Operators/)**  
  Mastering arithmetic, comparison, logical, assignment, identity (`is`), and membership (`in`) operators.
  
* **[04. Input/Output:](./04_Input_and_Output/)**  
  Mastering basic I/O operations using `input()` and `print()`, formatting with f-strings.

* **[05. Control Flow:](./05_Control_Flow/)**  
  Implementing conditionals utilizing `if`, `elif`, and `else` clauses.

* **[06. Iteration:](./06_Iteration/)**  
  Deep dive into `for` and `while` loops, iterating over sequences, and using control statements like `break`, `continue`, and `pass`.

---

## Hands-On Practice Tasks

To master these concepts, complete the following four tasks. Navigate to the respective sub-directories to write and test your code.

### Task 1.1: Build a Dynamic "User Profile" Generator

**Objective:** Practice variable assignment, basic data types (string, integer, float, boolean), and using the `input()` and `print()` functions.

Create a script that prompts the user for information and prints a formatted summary profile.

* **Where to write your code:** Navigate to the **[task_1_1_user_profile](./Tasks/task_1_1_user_profile/)** directory and write your solution inside the `user_profile.py` file.
* **Input Requirements:** Name (String), Age (Integer), Weight (Float), Employment Status (Boolean: Y/N).
* **Processing:** * Store input in correctly typed variables.
  * Convert the 'employed' input ('Y'/'N') into a Boolean (`True` / `False`).
  * Calculate BMI using a placeholder height (e.g., 1.75m).
* **Output:** Print a well-formatted summary using f-strings, clearly labeling all gathered and calculated data.

**How to test your code:**
Once you have written your solution, you can verify its logic using the provided automated test script. Open your terminal, ensure you are in the correct directory, and run the following commands:

```bash
cd Tasks/task_1_1_user_profile
python test_user_profile.py
```

---

### Task 1.2: The String Surgeon

**Objective:** Master string immutability, slicing `[start:stop:step]`, and built-in string methods (`strip`, `upper`, `replace`, `split`).

You have intercepted a messy, unformatted log entry from a legacy database. Your task is to clean and extract the relevant information using Python's string operations.

* **Where to write your code:** Navigate to the **[task_1_2_string_surgeon](./Tasks/task_1_2_string_surgeon/)** directory and write your solution inside the `string_surgeon.py` file.
* **Target String:**
  `log_entry = "   ERROR-CODE: 404 - file_not_found - admin_node_7   "`
* **Processing Steps:**
  1. **Clean:** Remove the leading and trailing whitespace.
  2. **Standardize:** Convert the entire cleaned string to uppercase.
  3. **Replace:** Replace all hyphens (`-`) with underscores (`_`).
  4. **Extract:** Slice the string to extract only the error number (`404`). Store this in a new variable.
  5. **Split:** Split the fully cleaned/replaced string into a list of words using the spaces as the delimiter.
* **Output Requirements:** Print the result of each step one by one so you can visually verify how the string transforms through the pipeline.

**How to test your code:**
Once you have written your solution, you can verify its logic using the automated test script located in the **[task_1_2_string_surgeon](./Tasks/task_1_2_string_surgeon/)** folder. Open your terminal, ensure you are in the correct directory, and run the following commands:

```bash
cd Tasks/task_1_2_string_surgeon
python test_string_surgeon.py
```

---

### Task 1.3: Develop a Comprehensive "Logic Gate Simulator"

**Objective:** Master `if`, `elif`, and `else` statements, and implement logical operators (`and`, `or`, `not`) and nested conditions.

Create a program that simulates fundamental logic gates (AND, OR, NOT, XOR).

* **Where to write your code:** Navigate to the **[task_1_3_logic_gate](./Tasks/task_1_3_logic_gate/)** directory and write your solution inside the `logic_gate.py` file.
* **Input:** Two boolean inputs (A and B, accepted as `True`/`False` or `1`/`0`).
* **Requirements:**
  * Implement checks for AND, OR, and NOT gates.
  * Implement an XOR gate using nested logic or combined operators (XOR is True only if A and B differ)
* **User Interaction:** Prompt the user to select a gate to test, take the necessary inputs, and print the resulting output.

**How to test your code:**
Once your solution is ready, verify its logic using the automated test script located in the **[task_1_3_logic_gate](./Tasks/task_1_3_logic_gate/)** folder. Open your terminal, ensure you are in the correct directory, and run:

```bash
cd Tasks/task_1_3_logic_gate
python test_logic_gate.py
```

---

### Task 1.4: Create an Automated "Password Strength Validator"

**Objective:** Practice using `for` and `while` loops, `break` and `continue` keywords, and iterating over strings.

Write a script that checks a user-provided password against complex rules. Use a `while` loop to keep prompting the user until a valid password is provided.

* **Where to write your code:** Navigate to the **[task_1_4_password_validator](./Tasks/task_1_4_password_validator/)** directory and write your solution inside the `password_validator.py` file.
* **Rules:** The password must meet all the following criteria:
  * Minimum length of 8 characters.
  * Contains at least one Uppercase letter.
  * Contains at least one Lowercase letter.
  * Contains at least one Digit.
  * Contains at least one Special Character (!@#$%^&).
* **Processing:** Use a `for` loop to iterate through the characters of the password and count rule fulfillment. Provide specific feedback to the user on which rules failed. Use the `break` keyword only when all conditions are met successfully.

**How to test your code:**
Once your solution is ready, verify its logic using the automated test script located in the **[task_1_4_password_validator](./Tasks/task_1_4_password_validator/)** folder. Open your terminal, ensure you are in the correct directory, and run:

```bash
cd Tasks/task_1_4_password_validator
python test_password_validator.py
```

---

## Mini Projects

### The Smart Cinema Ticketing System

**Scenario:**
You have been contracted to develop a terminal-based ticketing script for a boutique cinema. The cinema currently has a limited number of seats remaining, and your program must automatically process customer requests until the show is entirely sold out.

**Instructions:**
Write a complete Python script that satisfies all the following business logic and styling requirements.

* **Where to write your code:** Navigate to the **[01_cinema_ticketing](./Projects/01_cinema_ticketing/)** directory and write your solution inside the `cinema_ticketing.py` file.

1. Initialize the system state with a starting inventory of 5 available tickets and a boolean flag indicating the cinema is currently open.
2. Implement a loop that continuously processes incoming customer transactions as long as the cinema's status remains open.
3. During each iteration, prompt the user for their name and the exact number of tickets they wish to purchase. Ensure the requested ticket quantity is appropriately converted to an integer for calculation.
4. Implement conditional logic to handle the following three purchase scenarios:
    * **Valid Purchase:** If the requested quantity is greater than 0 and less than or equal to the currently available stock, process the transaction by deducting the tickets from the inventory. Display a formatted success message (e.g., *"Success! [Name] bought [X] tickets."*).
    * **Oversell Attempt:** If the customer requests more tickets than are currently available, deny the transaction and display an apology detailing the exact number of remaining seats.
    * **Invalid Input:** If the request is 0 or a negative number, display an error message stating the input is invalid.
5. After evaluating each transaction, verify the current inventory. If the available ticket count reaches 0, print a *"Sold out!"* message, update the cinema's status flag to closed, and safely exit the loop.
6. Ensure your code adheres to professional Python styling standards: use `snake_case` for all variable names, maintain strict indentation, and include a descriptive multi-line docstring at the very top of your script explaining its purpose.

**How to test your code:**
Once you have written your solution, you can verify its logic using the provided automated test script located in the **[01_cinema_ticketing](./Projects/01_cinema_ticketing/)** folder. Open your terminal, ensure you are in the correct directory, and run the following commands:

```bash
cd Projects/01_cinema_ticketing
python test_cinema_ticketing.py
```

### The Smart ATM Simulator

**Scenario:**
You have been tasked with developing a terminal-based Automated Teller Machine (ATM) simulator. The script must allow a user to continuously process withdrawal transactions from their account until their balance is completely depleted.

**Instructions:**
Write a complete Python script that satisfies all the following business logic and styling requirements.

* **Where to write your code:** Navigate to the **[02_atm_simulator](./Projects/02_atm_simulator/)** directory and write your solution inside the `atm_simulator.py` file.

1. Initialize the system state with a starting account balance of 200.0 and a boolean flag indicating the ATM session is currently active.
2. Implement a loop that continuously processes transaction requests as long as the ATM session remains active.
3. During each iteration, display the current balance and prompt the user to enter a withdrawal amount. Ensure the input is appropriately converted to a floating-point number for accurate financial calculations.
4. Implement conditional logic to handle the following three withdrawal scenarios:
    * **Valid Withdrawal:** If the requested amount is strictly greater than 0 and less than or equal to the current balance, process the transaction by deducting the funds from the account. Display a formatted success message showing the dispensed amount and the newly updated balance.
    * **Insufficient Funds:** If the requested amount exceeds the current balance, deny the transaction and display an error message detailing the maximum available funds.
    * **Invalid Input:** If the requested amount is 0 or negative, display an error message stating that the withdrawal amount must be strictly greater than zero.
5. After evaluating each transaction, verify the remaining account balance. If the balance reaches exactly 0.0, print an "Account empty" farewell message, update the ATM session flag to inactive, and safely exit the loop.
6. Ensure your code adheres to professional Python styling standards: use `snake_case` for all variable names, maintain strict indentation, and include a descriptive multi-line docstring at the very top of your script explaining its purpose.

**How to test your code:**
Once you have written your solution, you can verify its logic using the provided automated test script located in the **[02_atm_simulator](./Projects/02_atm_simulator/)** folder. Open your terminal, ensure you are in the correct directory, and run the following commands:

```bash
cd Projects/02_atm_simulator
python test_atm_simulator.py
```

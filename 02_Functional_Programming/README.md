# Module 02: Functional Programming & Error Handling

Welcome to Module 02. Up until now, our Python scripts have executed linearly from top to bottom. In this module, we transition to Functional Programming. By wrapping our logic into reusable, modular blocks called functions, we make our code cleaner, easier to test, and highly scalable.

We will also cover how to handle unexpected errors gracefully so your programs don't crash when users provide bad data.

## Topics Covered

* **[1. Function Fundamentals:](./01_Function_Fundamentals/)**  
  Defining functions, utilizing positional and keyword arguments, setting default parameters, and managing return values.
* **[2. Variable Scoping:](./02_Variable_Scoping/)**  
  Understanding the LEGB rule (Local, Enclosing, Global, Built-in) and how Python resolves variable access and lifetimes.
* **[3. Lambda & Higher-Order Functions:](./03_Lambda_and_Higher_Order_Functions/)**  
  Writing inline, anonymous functions and applying them dynamically using `map()` and `filter()`.
* **[4. Exception Handling:](./4_Exception_Handling/)**  
  Building robust applications that gracefully catch and handle unexpected user inputs or system errors using `try`, `except`, `else`, and `finally` blocks.

---

## Hands-On Practice Tasks

To master these concepts, complete the following four tasks. Navigate to the respective sub-directories to write and test your code.

### Task 2.1: The Planetary Weight Calculator

**Objective:** Practice defining functions, utilizing positional and keyword arguments, setting default parameters, and managing return values.

Create a modular script that calculates how much an object would weigh on different planets in our solar system.

* **Where to write your code:** Navigate to the **[task_2_1_planetary_calculator](./Tasks/task_2_1_planetary_calculator/)** directory and write your solution inside the `planetary_calculator.py` file.
* **Requirements:**
  * Define a function named `calculate_weight` that takes two parameters: `mass` (in kg) and `planet`.
  * Set the `planet` parameter to have a default value of `"Earth"`.
  * Inside the function, use conditional logic (`if/elif`) to multiply the mass by the correct gravity multiplier (Earth = 9.8, Mars = 3.71, Jupiter = 24.79).
  * The function must return the final calculated weight (do not print it directly inside the function).
* **Execution:** Call your function three times at the bottom of your script and print the results:
    1. Once using only a positional argument for a 100kg mass (relying on the default Earth value).
    2. Once using positional arguments for 100kg on "Mars".
    3. Once using explicit keyword arguments for "Jupiter" and 100kg.

**How to test your code:**

```bash
cd task_2_1_planetary_calculator
python test_planetary_calculator.py
```

---

### Task 2.2: Global Configuration Manager

**Objective:** Master variable scoping, the LEGB rule, and the `global` keyword to modify script-level state safely.

You are building a mock deployment script. The system starts in a "Development" state, and a function must safely transition it to "Production".

* **Where to write your code:** Navigate to the **[task_2_2_config_manager](./Tasks/task_2_2_config_manager/)** directory and write your solution inside the `config_manager.py` file.
* **Requirements:**
  * Define a global variable named `system_env` and set it to the string `"Development"`.
  * Define a function named `deploy_to_production()`.
  * Inside the function, use the `global` keyword to claim access to `system_env` and change its value to `"Production"`.
  * Create a nested function (a function inside `deploy_to_production`) named `log_deployment()`. Have it print: *"Deploying from Development to Production..."* using variables from the **Enclosing** scope if possible.
* **Execution:** Print the `system_env` variable, call the `deploy_to_production()` function, and then print `system_env` again to prove the global state was permanently changed.

**How to test your code:**

```bash
cd task_2_2_config_manager
python test_config_manager.py
```

---

### Task 2.3: The Data Pipeline Purifier

**Objective:** Write inline anonymous functions and apply them dynamically using the `map()` and `filter()` higher-order functions.

You have received a raw, messy list of sensor readings. Some readings are negative (which are impossible errors for this specific sensor), and the remaining valid readings need a conversion applied to them.

* **Where to write your code:** Navigate to the **[task_2_3_data_pipeline](./Tasks/task_2_3_data_pipeline/)** directory and write your solution inside the `data_pipeline.py` file.
* **Input Data:** `raw_sensor_data = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]`
* **Processing Steps:**
    1. **Filter:** Use the `filter()` function combined with a lambda expression to remove any values less than 0.0. Store the result in a new list called valid_data.
    2. **Map:** Use the `map()` function combined with a `lambda` expression to multiply all the remaining values in `valid_data` by `1.5` (simulating a calibration adjustment). Store the result in a list called `calibrated_data`.
* **Output:** Print the original list, the filtered list, and the final mapped list to the console.

**How to test your code:**

```bash
cd task_2_3_data_pipeline
python test_data_pipeline.py
```

---

### Task 2.4: The Unbreakable Calculator

**Objective:** Build robust applications that gracefully catch and handle unexpected user inputs using `try`, `except`, `else`, and `finally` blocks.

Create a division calculator that asks the user for a numerator and a denominator. Users are unpredictable and might type letters instead of numbers, or try to divide by zero. Your program must survive all of this without crashing.

* **Where to write your code:** Navigate to the **[task_2_4_unbreakable_calc](./Tasks/task_2_4_unbreakable_calc/)** directory and write your solution inside the `unbreakable_calc.py` file.
* **Requirements:**
  * Wrap your `input()` and division logic inside a `try` block.
  * Implement an `except` block specifically for `ValueError` (if the user types text). Print: *"Error: Please enter numbers only."*
  * Implement an `except` block specifically for `ZeroDivisionError`. Print: *"Error: Cannot divide by zero."*
  * Implement an `else` block that prints the successful result of the division (e.g., *"Success! The result is [X]"*).
  * Implement a `finally` block that prints: *"Calculation attempt complete."* regardless of success or failure.

**How to test your code:**

```bash
cd task_2_4_unbreakable_calc
python test_unbreakable_calc.py
```

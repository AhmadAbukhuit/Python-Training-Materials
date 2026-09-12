"""
Task 2.4: The Unbreakable Calculator
Objective: Build robust applications that gracefully catch and handle unexpected user inputs using try, except, else, and finally blocks.

Create a division calculator that asks the user for a numerator and a denominator. Users are unpredictable and might type letters instead of numbers, or try to divide by zero. Your program must survive all of this without crashing.

Where to write your code: Navigate to the task_2_4_unbreakable_calc directory and write your solution inside the unbreakable_calc.py file.
Requirements:
Wrap your input() and division logic inside a try block.
Implement an except block specifically for ValueError (if the user types text). Print: "Error: Please enter numbers only."
Implement an except block specifically for ZeroDivisionError. Print: "Error: Cannot divide by zero."
Implement an else block that prints the successful result of the division (e.g., "Success! The result is [X]").
Implement a finally block that prints: "Calculation attempt complete." regardless of success or failure.
"""

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Success! The result is {result}")
finally:
    print("Calculation attempt complete.")

'''
Task 2.3: The Data Pipeline Purifier
Objective: Write inline anonymous functions and apply them dynamically using the map() and filter() higher-order functions.

You have received a raw, messy list of sensor readings. Some readings are negative (which are impossible errors for this specific sensor), and the remaining valid readings need a conversion applied to them.

Where to write your code: Navigate to the task_2_3_data_pipeline directory and write your solution inside the data_pipeline.py file.
Input Data: raw_sensor_data = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]
Processing Steps:
Filter: Use the filter() function combined with a lambda expression to remove any values less than 0.0. Store the result in a new list called valid_data.
Map: Use the map() function combined with a lambda expression to multiply all the remaining values in valid_data by 1.5 (simulating a calibration adjustment). Store the result in a list called calibrated_data.
Output: Print the original list, the filtered list, and the final mapped list to the console.
'''

numbers = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]

# Keep only even numbers using filter()
filtered = list(filter(lambda x: x % 2 >= 0.0, numbers))

# Double every number using map()
calibrated_data = list(map(lambda x: x * 2, filtered))

# Step 3: Print results
print("Original:", numbers)
print("Filtered:", filtered)
print("Calibrated:", calibrated_data)

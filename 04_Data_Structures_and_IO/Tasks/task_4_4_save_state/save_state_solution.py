import json

def save_data(data_dict, filename):
    # Use 'w' mode to write/overwrite. The 'with' statement ensures it closes safely.
    with open(filename, "w") as file:
        json.dump(data_dict, file, indent=4)

def load_data(filename):
    # Use 'r' mode to read.
    with open(filename, "r") as file:
        data = json.load(file)
        return data
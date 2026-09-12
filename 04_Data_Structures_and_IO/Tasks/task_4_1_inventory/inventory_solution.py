def get_unique_items(item_list):
    # Convert to a set to remove duplicates, back to a list, and sort it
    unique_set = set(item_list)
    unique_list = list(unique_set)
    unique_list.sort()
    
    # Alternatively, you can do this in one line: 
    # return sorted(list(set(item_list)))
    
    return unique_list
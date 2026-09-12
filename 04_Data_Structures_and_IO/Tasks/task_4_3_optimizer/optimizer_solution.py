from collections import Counter

def filter_evens(numbers):
    # A list comprehension that iterates and filters in one line
    return [num for num in numbers if num % 2 == 0]

def get_top_word(word_list):
    # Pass the list directly into Counter
    word_counts = Counter(word_list)
    
    # most_common(1) returns a list containing a tuple: e.g., [('error', 3)]
    # We extract just the word itself by grabbing index [0][0]
    return word_counts.most_common(1)[0][0]
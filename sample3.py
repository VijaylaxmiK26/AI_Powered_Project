def read_file_lines(filename):
    """Reads a text file and returns a list of lines"""
    with open(filename, "r") as f:
        return f.readlines()

def filter_words(words, min_length):
    """Returns a list of words longer than min_length"""
    return [w for w in words if len(w) > min_length]

def flatten_list(nested_list):
    """Flattens a nested list"""
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat

def fibonacci_recursive(n):
    """Returns the nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

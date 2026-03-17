def add(a, b):
    """
    Summary of add function.
    
    Args:
        parameters: Description of parameters.
    
    Returns:
        Description of return value.
    
    """
    return a + b

def multiply(a, b):
    """
    Summary of multiply.
    
    Summary of add function.
        
        Args:
            parameters: Description of parameters.
        
        Returns:
            Description of return value.
    
    """
    result = 0
    for _ in range(b):
        result += a
    return result 

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """Calculates factorial recursively"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def greet(name):
    print(f"Hello, {name}!")
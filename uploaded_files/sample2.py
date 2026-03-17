def factorial(n):
    """
    Summary of factorial function.
    
    Parameters
    ----------
    parameters : type
        Description.
    
    Returns
    -------
    type
        Description of return value.
    
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
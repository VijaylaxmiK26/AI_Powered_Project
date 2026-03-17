# docstring_generator.py

def generate_docstring(func_name: str, style: str = "Google") -> str:
    """
    Generates a docstring for the given function name in the specified style.

    Args:
        func_name (str): The function name to document.
        style (str): The docstring style. One of "Google", "NumPy", "reST".

    Returns:
        str: Formatted docstring in the selected style.
    """

    # Google Style
    if style == "Google":
        doc = f'''Summary of {func_name}.

Summary of add function.
    
    Args:
        parameters: Description of parameters.
    
    Returns:
        Description of return value.
'''
        return doc

    # NumPy Style
    elif style == "NumPy":
        doc = f'''{func_name} summary.

Parameters
----------
param1 : type
    Description of param1
param2 : type
    Description of param2

Returns
-------
type
    Description of return value
'''
        return doc

    # reStructuredText (reST) Style
    elif style == "reST":
        doc = f'''{func_name} summary.

:Parameters:
    param1 (type) -- Description of param1
    param2 (type) -- Description of param2

:Returns:
    type -- Description of return value
'''
        return doc

    else:
        # Fallback to Google style
        return f"""Summary of {func_name}."""
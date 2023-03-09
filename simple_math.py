"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Calculates the addition of two numbers: a and b

    Parameters
    ----------
    a : first number
    b : second number

    Returns
    -------
    The result of the addition of a plus b

    Examples
    --------
    >>> simple_add(1,2)
    3
    >>> simple_add(5,14)
    19
    
    """
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....

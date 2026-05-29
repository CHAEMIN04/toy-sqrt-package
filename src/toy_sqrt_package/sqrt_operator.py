import math

def sqrt_operator(x):
    """
    Return the square root of a nonnegative number.

    If x is negative, stop immediately and raise ValueError.
    """
    if x < 0:
        raise ValueError(
            f"sqrt_operator() is undefined for negative inputs. Got x = {x}. Please enter a nonnegative number."
        )
    return math.sqrt(x)
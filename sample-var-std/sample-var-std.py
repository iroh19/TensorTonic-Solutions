import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    arr = np.array(x)
    centered = arr - np.mean(arr)
    varyans = np.sum(centered**2)/(arr.size-1)
    standart_sapma = np.sqrt(varyans)
    return {
        "variance" : float(varyans),
        "standard_deviation" : float(standart_sapma)
    }
    pass
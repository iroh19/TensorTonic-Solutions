import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:
    """
    Returns a 2D float64 array of zeros or ones with the requested shape.
    """
    if kind == "zeros":
        dizi = np.zeros(shape , dtype=np.float64)
        
    elif kind == "ones":
        dizi = np.ones(shape, dtype=np.float64)

    return dizi
    pass

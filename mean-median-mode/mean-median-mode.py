from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))

    counts = Counter(x)

    max_count = max(counts.values())

    modes = [num for num , count in counts.items() if count == max_count]

    mode_val = float(min(modes))

    return {

        "mean": mean_val ,
        "median" : median_val ,
        "mode" : mode_val
    }
    
    
    
    pass
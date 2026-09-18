import pandas as pd

def select_column(data, column):
    df = pd.DataFrame(data)
    values = list(df[column])
    length = len(values)
    
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    return {
        "values" : values,
        "length" : length
    }
    pass
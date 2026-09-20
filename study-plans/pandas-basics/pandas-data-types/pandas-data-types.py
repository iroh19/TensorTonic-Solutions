import pandas as pd

def data_types_overview(data):
    df = pd.DataFrame(data)
    dtype_series = df.dtypes.astype(str)
    dtypes = dtype_series.to_dict()
    type_counts= dtype_series.value_counts().to_dict()
    num_columns= len(df.columns)
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    return {
        "dtypes" : dtypes,
        "type_counts" : type_counts,
        "num_columns" : num_columns
    }
    pass
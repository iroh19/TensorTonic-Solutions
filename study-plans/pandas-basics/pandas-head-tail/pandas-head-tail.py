import pandas as pd

def head_tail(data: dict, n: int) -> dict:
    """
    Returns head and tail as dictionaries mapping columns to value lists.
    """
    df = pd.DataFrame(data)
    head_df=df.head(n)
    tail_df=df.tail(n)
    return {
        "head": {col: head_df[col].tolist() for col in df.columns},
        "tail": {col: tail_df[col].tolist() for col in df.columns}
    }
    pass

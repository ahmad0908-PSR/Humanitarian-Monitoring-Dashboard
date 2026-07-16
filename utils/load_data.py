import pandas as pd
from pathlib import Path

def load_data():
    """
    we simply load the humanitarian dataset and return it as a Pandas DataFrame.

    """
    data_path = Path(__file__).parent.parent / "data" / "Humanitarian_data.csv"
    df = pd.read_csv(data_path)

    return df 
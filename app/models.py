import pandas as pd

# This will hold the in-memory dataset across requests
class DataStore:
    raw_data: pd.DataFrame = None
    cleaned_data: pd.DataFrame = None

store = DataStore()

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Clean up cancelled or zero-quantity rows
    df = df[(df['Qty'] > 0) & (~df['Status'].str.contains("Cancelled", na=False))]

    # Normalize columns
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

    df = df.dropna(subset=['Date', 'Qty', 'Amount'])

    return df

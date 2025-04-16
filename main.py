import pandas as pd
import numpy as np

def parse_volume(volume_str):
    """Converts volume strings like '1.23M' or '45.6K' to float."""
    volume_str = str(volume_str).strip()
    if volume_str == '-':  # Handle potential missing values represented as '-'
        return np.nan
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}
    suffix = volume_str[-1]
    if suffix in multipliers:
        value = float(volume_str[:-1]) * multipliers[suffix]
    else:
        try:
            value = float(volume_str) # Assuming no suffix means base units
        except ValueError:
            value = np.nan # Handle cases that are not convertible
    return value

def main():
    df = pd.read_csv("btc_price_history.csv")

    # Rename columns according to schema and desired output
    df = df.rename(columns={
        'Date': 'timestamp',
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Price': 'price', 
        'Vol.': 'volume',
        'Change %': 'change_percentage'
    })

    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%m/%d/%Y')

    # Clean and convert numeric columns (removing commas)
    numeric_cols = ['open', 'high', 'low', 'price']
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(',', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce') # errors='coerce' turns unparseable into NaN

    df['volume'] = df['volume'].apply(parse_volume)
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

    df['change_percentage'] = df['change_percentage'].astype(str).str.replace('%', '', regex=False)
    df['change_percentage'] = pd.to_numeric(df['change_percentage'], errors='coerce') # Keep as percentage

    print("--- DataFrame Info Before Save ---")
    df.info()
    print("\nDataFrame Head:")
    print(df.head())

    # Save to Parquet
    parquet_file = "btc_price_history.parquet"
    print(f"\nSaving DataFrame to {parquet_file}...")
    df.to_parquet(parquet_file, index=False)
    print("Save complete.")

    # Load from Parquet to verify
    print(f"\nLoading DataFrame from {parquet_file}...")
    df_loaded = pd.read_parquet(parquet_file)
    print("Load complete.")

    print("\n--- Loaded DataFrame Info ---")
    df_loaded.info()
    print("\nLoaded DataFrame Head:")
    print(df_loaded.head())

    # Print min and max values for timestamp and corresponding price
    print(f"Min timestamp: {df['timestamp'].iloc[-1]}")
    print(f"Max timestamp: {df['timestamp'].iloc[0]}")
    print(f"Price at min timestamp: {df['price'].iloc[-1]}")
    print(f"Price at max timestamp: {df['price'].iloc[0]}")

if __name__ == "__main__":
    main()

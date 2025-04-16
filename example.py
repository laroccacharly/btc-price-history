import pandas as pd


url = "https://github.com/laroccacharly/btc-price-history/raw/refs/heads/main/btc_price_history.parquet"

print(f"Downloading and reading parquet file from: {url}")

df = pd.read_parquet(url)

print("\n--- DataFrame Info ---")
df.info()

print("\n--- DataFrame Head ---")
print(df.head())

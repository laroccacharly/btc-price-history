# Bitcoin Price History 

This project processes historical Bitcoin price data from a CSV file (`btc_price_history.csv`), cleans it, converts data types, and saves the result into a Parquet file (`btc_price_history.parquet`) for efficient storage and analysis.

## Parquet File Structure (`btc_price_history.parquet`)

The resulting Parquet file contains the cleaned Bitcoin price data with the following columns and data types:

*   **timestamp**: Date of the record (datetime64[ns])
*   **open**: Opening price in USD (float64)
*   **high**: Highest price in USD for the day (float64)
*   **low**: Lowest price in USD for the day (float64)
*   **price**: Closing price in USD (float64)
*   **volume**: Trading volume (numeric count) (float64)
*   **change_percentage**: Daily price change percentage (float64)

## Data Range

Based on the processed data:

*   **Minimum Timestamp**: 2011-10-06
*   **Maximum Timestamp**: 2025-04-15
*   **Price at Minimum Timestamp**: 4.7 USD
*   **Price at Maximum Timestamp**: 84175.9 USD


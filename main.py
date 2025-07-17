import yfinance as yf
import os
import pandas as pd

# Directory settings
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# List of stock symbols
stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

# Date range
start_date = "2020-01-01"
end_date = "2025-05-29"

def download_stock_data(symbol):
    try:
        print(f"Downloading data for {symbol}...")
        stock_data = yf.download(symbol, start=start_date, end=end_date)

        # Check if data was successfully downloaded
        if not stock_data.empty:
            # Reset index to make 'Date' a column
            stock_data.reset_index(inplace=True)

            # Reorder columns to match the required format
            stock_data = stock_data[["Date", "Open", "High", "Low", "Close", "Volume"]]

            # Ensure the Date column is properly formatted
            stock_data["Date"] = pd.to_datetime(stock_data["Date"]).dt.strftime('%Y-%m-%d')

            # Save to CSV without extra headers or indices
            file_path = os.path.join(data_folder, f"{symbol}_stock_data.csv")
            
            # Save to CSV with a single header row
            stock_data.to_csv(file_path, index=False)
            print(f"Data for {symbol} saved to {file_path}")
        else:
            print(f"No data found for {symbol}.")
    except Exception as e:
        print(f"Error downloading data for {symbol}: {e}")

# Download data for each stock symbol
for symbol in stock_symbols:
    download_stock_data(symbol)

print("\nData download completed.")

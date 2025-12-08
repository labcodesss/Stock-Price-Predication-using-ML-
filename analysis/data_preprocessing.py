import pandas as pd
import os

data_folder = "data"
processed_folder = "data/processed"
os.makedirs(processed_folder, exist_ok=True)

def preprocess_data(symbol):
    try:
        file_path = os.path.join(data_folder, f"{symbol}_stock_data.csv")
        data = pd.read_csv(file_path, parse_dates=["Date"], dayfirst=True)
        data.set_index("Date", inplace=True)

        # Check if the 'Close' column exists before calculating moving averages
        if "Close" in data.columns:
            # Add 50-day moving average
            data['MA_50'] = data['Close'].rolling(window=50).mean()

            # Add 200-day moving average
            data['MA_200'] = data['Close'].rolling(window=200).mean()
        else:
            print(f"Warning: 'Close' column not found in {symbol} data.")
        
        # Save the processed data
        processed_file_path = os.path.join(processed_folder, f"{symbol}_processed.csv")
        data.to_csv(processed_file_path)
        print(f"Processed data saved for {symbol}: {processed_file_path}")

    except Exception as e:
        print(f"Error processing data for {symbol}: {e}")

# List of stock symbols
stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

# Process data for each stock symbol
for symbol in stock_symbols:
    preprocess_data(symbol)

print("\nData preprocessing completed.")

import os
import pandas as pd

# Directory for processed data
data_folder = "data/processed"

# List of stock symbols
stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

def calculate_cumulative_return(symbol):
    try:
        # Load processed data
        file_path = os.path.join(data_folder, f"{symbol}_processed.csv")
        data = pd.read_csv(file_path)

        # Calculate Cumulative Return
        initial_price = data['Close'].iloc[0]
        final_price = data['Close'].iloc[-1]
        cumulative_return = ((final_price / initial_price) - 1) * 100

        print(f"{symbol}: Cumulative Return: {cumulative_return:.2f}%")
    except Exception as e:
        print(f"Error processing {symbol}: {e}")

# Execute for each symbol
for symbol in stock_symbols:
    calculate_cumulative_return(symbol)

print("\nInvestment Analysis Completed.")

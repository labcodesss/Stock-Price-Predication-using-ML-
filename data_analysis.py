# data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import os

data_folder = "data/processed"
output_folder = "visualizations"
os.makedirs(output_folder, exist_ok=True)

stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

def plot_stock_data(symbol):
    file_path = os.path.join(data_folder, f"{symbol}_processed.csv")
    
    # Load data with Date as index
    data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    
    plt.figure(figsize=(14, 7))
    plt.plot(data["Close"], label="Close Price", color="blue")
    
    # Plot MA_50 if it exists
    if "MA_50" in data.columns:
        plt.plot(data["MA_50"], label="50-Day MA", color="green")
    else:
        print(f"Warning: 'MA_50' not found in {symbol} data.")
    
    # Plot MA_200 if it exists
    if "MA_200" in data.columns:
        plt.plot(data["MA_200"], label="200-Day MA", color="red")
    else:
        print(f"Warning: 'MA_200' not found in {symbol} data.")
    
    plt.title(f"{symbol} Stock Price and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    
    plot_path = os.path.join(output_folder, f"{symbol}_plot.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot for {symbol} saved to {plot_path}")

for symbol in stock_symbols:
    plot_stock_data(symbol)

print("\nData visualization completed.")

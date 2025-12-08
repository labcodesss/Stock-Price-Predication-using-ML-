import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import datetime, timedelta

# Directory settings
data_folder = "data/processed"
models_folder = "models"
os.makedirs(models_folder, exist_ok=True)

# List of stock symbols
stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]

# Number of days to predict
prediction_days = 5

def apply_linear_regression(symbol):
    try:
        print(f"\nProcessing predictions for {symbol}...")
        
        # Load processed data
        file_path = os.path.join(data_folder, f"{symbol}_processed.csv")
        data = pd.read_csv(file_path, parse_dates=["Date"])
        
        # Prepare data for training
        data['Prediction'] = data['Close'].shift(-prediction_days)
        X = np.array(data[['Close']][:-prediction_days])
        y = np.array(data['Prediction'][:-prediction_days])
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Evaluate model
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        print(f"Training R²: {train_score:.2f}")
        print(f"Testing R²: {test_score:.2f}")
        print(f"MAE: {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")
        
        # Predict future prices
        X_future = np.array(data['Close'].tail(prediction_days)).reshape(-1, 1)
        predictions = model.predict(X_future)
        
        # Generate prediction dates (next business days)
        last_date = data['Date'].iloc[-1]
        prediction_dates = [last_date + timedelta(days=i) for i in range(1, prediction_days+1)]
        
        # Create prediction dataframe
        predictions_df = pd.DataFrame({
            'Date': prediction_dates,
            'Prediction': predictions,
            'Model_R2': test_score,
            'MAE': mae,
            'RMSE': rmse
        })
        
        # Save predictions to models folder
        prediction_path = os.path.join(models_folder, f"{symbol}_predictions.csv")
        predictions_df.to_csv(prediction_path, index=False)
        print(f"Predictions saved to {prediction_path}")
        
        # Print predictions
        print(f"\nPredicted prices for {symbol}:")
        for date, pred in zip(prediction_dates, predictions):
            print(f"{date.strftime('%Y-%m-%d')}: ${pred:.2f}")
            
        return True
        
    except Exception as e:
        print(f"Error processing {symbol}: {e}")
        return False

def main():
    print("Starting stock price prediction...")
    success_count = 0
    
    for symbol in stock_symbols:
        if apply_linear_regression(symbol):
            success_count += 1
    
    print(f"\nPrediction completed for {success_count}/{len(stock_symbols)} stocks")
    print("Prediction Model Analysis Completed.")

if __name__ == "__main__":
    main()
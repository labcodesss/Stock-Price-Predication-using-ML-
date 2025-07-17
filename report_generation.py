from fpdf import FPDF
import os
import pandas as pd
from datetime import datetime, timedelta

# Configuration - Set to False to disable crossover signals
SHOW_CROSSOVER_SIGNALS = False  

def generate_report(stock_symbol):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Stock Price Analysis Report", ln=True, align="C")
    pdf.ln(10)
    
    # Stock Information Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, f"Stock: {stock_symbol}", ln=True)
    pdf.ln(5)
    
    # Get current date for report
    report_date = datetime.now().strftime('%Y-%m-%d')
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Report Date: {report_date}", ln=True)
    pdf.ln(10)
    
    # 1. Analysis Summary from investment_analysis.py
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Performance Analysis:", ln=True)
    pdf.set_font("Arial", '', 12)
    
    try:
        # Get cumulative return from investment analysis
        file_path = os.path.join("data/processed", f"{stock_symbol}_processed.csv")
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            initial_price = data['Close'].iloc[0]
            final_price = data['Close'].iloc[-1]
            cumulative_return = ((final_price / initial_price) - 1) * 100
            
            # Get recent price movement
            recent_change = ((data['Close'].iloc[-1] - data['Close'].iloc[-30]) / data['Close'].iloc[-30]) * 100
            
            analysis_summary = (
                f"Cumulative Return: {cumulative_return:.2f}%\n"
                f"Recent 30-day Change: {recent_change:.2f}%\n"
                f"Current Price: ${final_price:.2f}\n"
                f"50-Day MA: ${data['MA_50'].iloc[-1]:.2f}\n"
                f"200-Day MA: ${data['MA_200'].iloc[-1]:.2f}"
            )
            pdf.multi_cell(0, 10, analysis_summary)
        else:
            pdf.multi_cell(0, 10, "Performance data not available")
    except Exception as e:
        pdf.multi_cell(0, 10, f"Error loading performance data: {str(e)}")
    pdf.ln(5)
    
    # 2. Model Performance from prediction_model.py
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Price Predictions:", ln=True)
    pdf.set_font("Arial", '', 12)
    
    try:
        # Get predictions
        pred_file = os.path.join("models", f"{stock_symbol}_predictions.csv")
        if os.path.exists(pred_file):
            pred_data = pd.read_csv(pred_file)
            predictions_text = "Next 5 days predicted prices:\n"
            for i, row in pred_data.iterrows():
                predictions_text += f"{row['Date']}: ${row['Prediction']:.2f}\n"
            pdf.multi_cell(0, 10, predictions_text)
        else:
            pdf.multi_cell(0, 10, "Prediction data not available")
    except Exception as e:
        pdf.multi_cell(0, 10, f"Error loading prediction data: {str(e)}")
    pdf.ln(5)
    
    # 3. Trading Signals (Conditional based on config)
    if SHOW_CROSSOVER_SIGNALS:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Trading Signals:", ln=True)
        pdf.set_font("Arial", '', 12)
        
        try:
            if os.path.exists(file_path):
                # Detect recent moving average crossovers
                data['MA_50'] = data['MA_50'].fillna(method='bfill')
                data['MA_200'] = data['MA_200'].fillna(method='bfill')
                
                # Check for golden cross (50MA crossing above 200MA)
                golden_cross = (data['MA_50'].iloc[-2] < data['MA_200'].iloc[-2]) and (data['MA_50'].iloc[-1] > data['MA_200'].iloc[-1])
                
                # Check for death cross (50MA crossing below 200MA)
                death_cross = (data['MA_50'].iloc[-2] > data['MA_200'].iloc[-2]) and (data['MA_50'].iloc[-1] < data['MA_200'].iloc[-1])
                
                signals = []
                if golden_cross:
                    signals.append("GOLDEN CROSS DETECTED (Bullish Signal)")
                if death_cross:
                    signals.append("DEATH CROSS DETECTED (Bearish Signal)")
                
                if not signals:
                    signals.append("No strong crossover signals detected")
                    
                signals_text = "\n".join(signals)
                pdf.multi_cell(0, 10, signals_text)
        except Exception as e:
            pdf.multi_cell(0, 10, f"Error generating trading signals: {str(e)}")
        pdf.ln(5)
    
    # Add visualization to the report
    vis_path = os.path.join("visualizations", f"{stock_symbol}_plot.png")
    if os.path.exists(vis_path):
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Price Chart:", ln=True)
        pdf.image(vis_path, x=10, w=190)
    
    # Save report
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    
    output_path = os.path.join(reports_dir, f"{stock_symbol}_stock_report.pdf")
    pdf.output(output_path)
    print(f"Report saved: {output_path}")

if __name__ == "__main__":
    # Ensure all processing has been done first
    stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG"]
    
    for symbol in stock_symbols:
        generate_report(symbol)
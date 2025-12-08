📌 Stock Price Analysis & Prediction Using Machine Learning

This project focuses on analyzing historical stock market data and forecasting future stock prices using machine learning techniques. The system retrieves stock data, preprocesses it, performs exploratory analysis, builds prediction models, generates visual insights, and finally produces automated PDF reports for five major companies:

🔹 Apple (AAPL)
🔹 Microsoft (MSFT)
🔹 Tesla (TSLA)
🔹 Amazon (AMZN)
🔹 Google (GOOG)

🚀 Project Features
Feature	                         Description
📥 Automated Data Collection	   Stock data fetched using Yahoo Finance API.
🧹 Data Preprocessing            Calculation of Moving Averages (50 & 200 days) and formatting.
📊 Visualization	               Plots of stock trends and moving averages stored in /visualizations.
🤖 Machine Learning Model	       Linear Regression used for 5-day price prediction.
📈 Investment Metrics	           Cumulative returns and trend analysis.
📄 PDF Report Generation	       Auto-generated report for each company stored in /reports.

🛠️ Technologies Used
Category	       Tools/Libraries
Programming	     Python
Data Handling	   Pandas, NumPy
Machine Learning Scikit-Learn (Linear Regression)
Visualization	   Matplotlib
API/Data Source	 Yahoo Finance (yfinance)
Reporting	       FPDF

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/StockPricePrediction.git
cd StockPricePrediction

2️⃣ Create Virtual Environment (Optional)
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Project
Run the scripts step-by-step:
Step	  Run Command	                   Output
1	      python main.py	              Downloads raw stock data
2	      python data_preprocessing.py	Adds MA_50 & MA_200
3	      python data_analysis.py	      Saves stock trend visualizations
4	      python investment_analysis.py	Displays cumulative returns
5	      python prediction_model.py	  Generates stock predictions
6	      python report_generation.py	  Creates final PDF reports

📈 Example Output (Prediction & Returns)
AAPL: Cumulative Return: 246.45%
MSFT: Cumulative Return: 176.53%
TSLA: Cumulative Return: 1355.20%
AMZN: Cumulative Return: 133.19%
GOOG: Cumulative Return: 182.85%

📌 Future Improvements

✔ Replace Linear Regression with advanced models (LSTM, ARIMA, Random Forest)
✔ Deploy web dashboard using Streamlit or Flask
✔ Add real-time live streaming stock data
✔ Add sentiment analysis from Twitter/News API

📚 References

Yahoo Finance API
Scikit-Learn Documentation
Matplotlib & Pandas Official Docs

👩‍💻 Author

Name: Mouna C
Domain: Data Science
Internship Organization: Plasmid

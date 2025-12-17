📊 Stock Price Correlation Analysis (Python + NumPy)
---
📌 Overview

This project analyzes stock price movements to identify how different stocks move together over time.
It calculates correlation using NumPy, applies OOP concepts, and visualizes relationships using charts.
---
🚀 Features

Load and validate historical stock prices

Calculate stock correlations using NumPy

Identify strongly correlated stock pairs

Visualize data with:

📉 Dual line charts

🔥 Correlation heatmap

Save results in JSON format

🧠 Concepts Used

Python OOP (StockPair class)

NumPy (np.corrcoef)

Decorators (input validation)

Lambda functions

List comprehensions

Data visualization (Matplotlib, Seaborn)
---
📂 Project Structure
├── stock_correlation_main.py
├── stock_pair_class.py
├── stock_utils.py
├── stock_prices.csv
├── correlation_matrix.json
---
📊 Sample Data (stock_prices.csv)
Date,AAPL,MSFT,GOOGL
2024-01-01,185,370,140
2024-01-02,187,372,142
2024-01-03,186,369,141
---
▶️ How to Run
pip install pandas numpy matplotlib seaborn
python stock_correlation_main.py
---
📈 Output

Correlation heatmap of all stocks

Line chart comparison of highly correlated stock pairs

Saved correlation matrix in JSON format

🏁 Conclusion

This project demonstrates real-world financial data analysis using NumPy-based correlation, clean OOP design, and meaningful visualizations.

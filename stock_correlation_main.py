import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from stock_pair_class import StockPair
from stock_utils import load_stock_data, save_correlation_matrix


# Load data
df = pd.read_csv("stock_prices.csv", index_col="Date", parse_dates=True)
df = load_stock_data(df)


# Correlation matrix
# Correlation matrix using NumPy
corr_matrix = pd.DataFrame(
np.corrcoef(df.values.T),
index=df.columns,
columns=df.columns
)
save_correlation_matrix(corr_matrix.to_dict())


# Heatmap visualization
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Stock Correlation Heatmap")
plt.show()


# Strongly correlated pairs
threshold = 0.7
stocks = df.columns
pairs = [
(stocks[i], stocks[j])
for i in range(len(stocks))
for j in range(i+1, len(stocks))
if corr_matrix.iloc[i, j] > threshold
]


# Analyze and plot
for s1, s2 in pairs:
    pair = StockPair(s1, s2, df)
    pair.calculate_correlation()
    pair.plot_pairs()
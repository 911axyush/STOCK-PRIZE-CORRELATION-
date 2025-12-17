import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class StockPair:
    def __init__(self, stock1, stock2, prices_df):
        self.stock1 = stock1
        self.stock2 = stock2
        self.prices_df = prices_df
        self.correlation = None


    def load_prices(self):
        return self.prices_df[[self.stock1, self.stock2]]


    def calculate_correlation(self):
        data = self.load_prices()
    # Using NumPy for correlation
        s1  = data[self.stock1].values
        s2 = data[self.stock2].values
        self.correlation = np.corrcoef(s1, s2)[0, 1]
        return self.correlation


    def plot_pairs(self):
        data = self.load_prices()
        data.plot(title=f"{self.stock1} vs {self.stock2}")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()


def save_analysis(self):
    return {
"stock1": self.stock1,
"stock2": self.stock2,
"correlation": self.correlation
}
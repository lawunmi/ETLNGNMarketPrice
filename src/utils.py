from matplotlib import pyplot as plt
import pandas as pd

def dataAnalysis(data):
    print("Total number of valid records: ", len(data.drop_duplicates()))
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    print("\nAverage Price per Product: ", data.groupby('product')['price'].mean())
    mktAvg = data.groupby('market')['price'].mean()
    print("\nMost Expensive Market(average price): ", mktAvg.idxmax(), mktAvg.max())
    print("\nDistribution of price categories: ", data['price_category'].value_counts())
    totalSales = data.groupby('product')['price'].sum()
    print("Product with Highest Sales Value: ", totalSales.idxmax(), totalSales.max())


def avgProductPriceChart(data):
    #data['price'] = pd.to_numeric(data['price'], errors='coerce')
    data.groupby('product')['price'].mean().plot(
        kind='bar',
        x='Product',
        y='Price',
        title='Average price for each product',
    )
    plt.show()
    return None

def avgMarketPriceChart(data):
    data.groupby('market')['price'].mean().plot(
        kind='bar',
        x='Market',
        y='Price',
        title='Average price for each market',
    )
    plt.show()
    return None

def priceCategoryChart(data):
    data['price_category'].value_counts().plot(
        kind='pie',
        title='Price Category',
        legend=True,
        autopct='%1.1f%%'
    )
    plt.show()
    return None


import logging
import pandas as pd

logging.info("Starting ETL NG Market pipeline...")

logging.info("Data extraction started...")

#data set loaded using pandas
def fetchData():
    marketData = pd.read_csv('../market_data.csv')
    logging.info("Data extracted successfully...")
    return marketData

data = fetchData()
#first 10 rows display
print(data.head(10))

#display shape(number of rows and columns)
print(data.shape)

#display column names
print(data.columns)

logging.info("Data extraction completed...")

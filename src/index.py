import logging

#logging
logging.basicConfig(
    filename='../logs/market_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from MarketNg.config.db import connectDB
from MarketNg.src.extract import fetchData
from MarketNg.src.load import loadData
from MarketNg.src.transform import dataTransformation
from utils import *

def runPipeline():
    #extraction
    data = fetchData()
    logging.info("Data extracted successfully...")

    #transformation
    dataTransformation(data)

    #load
    conn = connectDB()
    loadData(conn, data)

    #analysis
    dataAnalysis(data)
    avgProductPriceChart(data)
    avgMarketPriceChart(data)
    priceCategoryChart(data)


runPipeline()




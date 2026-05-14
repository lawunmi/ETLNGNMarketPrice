import logging
import pandas as pd

logging.info("Data cleaning and transformation started...")

def priceCategory(price):
    if price <= 40000:
        return "Cheap"
    elif price <= 55000:
        return "Moderate"
    else:
        return "Expensive"

def marketType(market):
    if market == "Ibadan":
        return "Semi-urban"
    else:
        return "Urban"

def priceScore(row):
    if row['price_category'] == "Expensive":
        return row['price'] * 3
    elif row['price_category'] == "Moderate":
        return row['price'] * 2
    else:
        return row['price'] * 1

def dataTransformation(data):
    # handling missing & invalid values
    data.replace(["invalid", "not_available"], 0, inplace=True)
    data.fillna(0, inplace=True)

    #formatting
    data['market'] = data['market'].str.strip()
    data['market'] = data['market'].str.title()
    data['product'] = data['product'].str.strip()

    #Datatype conversion
    data['price'] = pd.to_numeric(data['price'])

    #remove duplicate
    duplicateRemoval = data.drop_duplicates()
    logging.info("Data cleaning completed...")

    #SECTION C: FEATURE ENGINEERING
    logging.info("Feature engineering started...")

    data['price_category'] = data['price'].apply(priceCategory)
    data['market_type'] = data['market'].apply(marketType)
    data['price_score'] = data.apply(priceScore, axis=1)

    #data['price_score'] = data['price_category'].apply(lambda x: data['price'] * 3 if x == "Expensive" else data['price'] * 2 if x == "Moderate" else data['price'] * 1)

    return data

    logging.info("Feature engineering completed...")

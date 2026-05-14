import logging

def loadData(conn, data):
    try:
        cursor = conn.cursor()
        for _, row in data.iterrows():
            cursor.execute('''
                INSERT INTO mktdata(market, product, price, date, price_category, market_type)
                VALUES(%s, %s, %s, %s, %s, %s)
            ''', (
                str(row['market']),
                str(row['product']),
                float(row['price']),
                str(row['date']),
                str(row['price_category']),
                str(row['market_type'])
            ))
        conn.commit()
        cursor.close()
        conn.close()

        logging.info("Data inserted into MarketNg")
        return True
    except Exception as e:
        logging.error(e)
        return False
import logging
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
def connectDB():
    connection = None
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        print("Connected to PostgreSQL database...")
    except psycopg2.Error as e:
        logging.error(f"Error {e} occurred while trying to connect to the database")
    return connection
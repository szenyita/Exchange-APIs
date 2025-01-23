import requests
import decimal
from api_endpoints import exchangerates_api
from db_config import cursor

def exchangerates():
    exchangerates_data = requests.get(exchangerates_api).json()

    for currency in exchangerates_data["rates"]:
        table = "exchangerates_" + currency.lower()

        create_table  = (
            f"""
            CREATE TABLE IF NOT EXISTS {table} (
                timestamp INT PRIMARY KEY,
                rate DECIMAL(65, 30)
            )
            """
        )
        cursor.execute(create_table)

        insert_record = (
            f"""
            INSERT INTO {table} (timestamp, rate) VALUES
            """ + "(%s, %s)"
        )
        cursor.execute(insert_record, (exchangerates_data["timestamp"], decimal.Decimal(str(exchangerates_data["rates"][currency])) / decimal.Decimal(str(exchangerates_data["rates"]["USD"])),))
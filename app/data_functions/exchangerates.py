import requests
from decimal import Decimal, getcontext
from config.api_endpoints import exchangerates_api
from config.db_config import cursor

def exchangerates():
    getcontext().prec = 30

    try:
        exchangerates_data = requests.get(exchangerates_api).json()
    except:
        return False

    if exchangerates_data["success"] == False:
        return False

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
        cursor.execute(insert_record, (exchangerates_data["timestamp"], Decimal(str(exchangerates_data["rates"][currency])) / Decimal(str(exchangerates_data["rates"]["USD"])),))
    
    return True
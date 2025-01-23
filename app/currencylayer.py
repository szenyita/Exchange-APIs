import requests
from api_endpoints import currencylayer_api
from db_config import cursor

def currencylayer():
    currencylayer_data = requests.get(currencylayer_api).json()

    for currency in currencylayer_data["rates"]:
        table = "currencylayer_" + currency[3:].lower()

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
        cursor.execute(insert_record, (currencylayer_data["timestamp"], currencylayer_data["rates"][currency],))
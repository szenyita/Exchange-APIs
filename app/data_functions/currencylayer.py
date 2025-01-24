import requests
from decimal import Decimal, getcontext
from config.api_endpoints import currencylayer_api
from config.db_config import cursor
from config.crypto_symbols import crypto_symbols

def currencylayer():
    getcontext().prec = 30

    try:
        currencylayer_data = requests.get(currencylayer_api).json()
    except:
        return False

    if currencylayer_data["success"] == False:
        return False

    for currency in currencylayer_data["quotes"]:
        if not currency.isalpha():
            continue
        
        table = "currencylayer_" + currency[3:].lower()
        
        try:

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

            if currency[3:].upper() in crypto_symbols:
                cursor.execute(insert_record, (currencylayer_data["timestamp"], 1 / Decimal(str(currencylayer_data["quotes"][currency])),))
            else:
                cursor.execute(insert_record, (currencylayer_data["timestamp"], currencylayer_data["quotes"][currency],))
        
        except:
            return False
    
    return True
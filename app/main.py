import schedule
import time
from data_functions.currencylayer import currencylayer
from data_functions.exchangerates import exchangerates

def main():
    currencylayer_success = currencylayer()
    exchangerates_success = exchangerates()

    while not currencylayer_success or not exchangerates_success:
        if not currencylayer_success:
            currencylayer_success = currencylayer()
        if not exchangerates_success:
            exchangerates_success = exchangerates()

        time.sleep(5 * 60)


schedule.every().day.at("00:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
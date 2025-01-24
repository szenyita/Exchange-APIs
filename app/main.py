import schedule
import time
from data_functions.currencylayer import currencylayer
from data_functions.exchangerates import exchangerates

currencylayer_success, exchangerates_success = False, False

def main():
    global currencylayer_success, exchangerates_success
    currencylayer_success = currencylayer()
    exchangerates_success = exchangerates()

schedule.every().day.at("00:00").do(main)

while True:
    schedule.run_pending()

    while not currencylayer_success or not exchangerates_success:
        if not currencylayer_success:
            currencylayer_success = currencylayer()
        if not exchangerates_success:
            exchangerates_success = exchangerates()

        time.sleep(5 * 60)

    time.sleep(1)
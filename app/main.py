import schedule
import time
from app.data_functions.currencylayer import currencylayer
from app.data_functions.exchangerates import exchangerates

currencylayer_retry, exchangerates_retry = None

def main():
    global currencylayer_retry, exchangerates_retry

    currencylayer_success = currencylayer()
    exchangerates_success = exchangerates()

    if not currencylayer_success and currencylayer_retry is None:
        currencylayer_retry = schedule.every(5).minutes.do(currencylayer)
    elif currencylayer_retry is not None:
        schedule.cancel_job(currencylayer_retry)
    
    if not exchangerates_success and exchangerates_retry is None:
        exchangerates_retry = schedule.every(5).minutes.do(exchangerates)
    elif exchangerates_retry is not None:
        schedule.cancel_job(exchangerates_retry)

schedule.every().day.at("00:00").do(main).tag("daily")

while True:
    schedule.run_pending()
    time.sleep(1)
import requests

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (6min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

stock_prices = {}
symbol = "hello"
price = get_stock_data()
if price is not None:
    stock_prices[symbol] = price
    print(f"{symbol}: {price}")

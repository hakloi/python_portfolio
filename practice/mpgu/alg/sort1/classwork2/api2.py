# 1. Изучите документацию API по ссылке 
# https://developers.binance.com/docs/binance-spot-api-docs/rest-api/public-api-endpoints
# 2. С помощью данного API выгрузите исторические котировки Биткоина, 
# Эфириума и еще одной монеты по вашему выбору. Обратите внимание на 
# Kline/Candlestick data endapoint.Выберите интервал в 1 день.
# 3. Скомпонуйте выгруженные данные в csvфайлы с заголовком.
# 4. На основе этих данных вычислите среднегодовую доходность каждой из монет 
# начиная с 2014 года (или года появления монеты), а также доходность по годам. 
# Скомпонуйте полученные данные в csv файл и пришлите его вместе с решением.


import requests
import csv
from datetime import datetime
import pandas as pd
import time

def get_historical_data(symbol, interval, start_time, end_time):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": int(start_time.timestamp() * 1000),
        "endTime": int(end_time.timestamp() * 1000),
        "limit": 1000
    }
    data = []
    
    while True:
        response = requests.get(url, params=params)
        klines = response.json()
        if not klines:
            break
        data.extend(klines)
        params["startTime"] = klines[-1][0] + 1
        time.sleep(1)
    
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        for kline in data:
            date = datetime.fromtimestamp(kline[0] / 1000).strftime('%Y-%m-%d')
            writer.writerow([date, kline[1], kline[2], kline[3], kline[4], kline[5]])

def calculate_annual_returns(filename):
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Close'] = df['Close'].astype(float)
    
    yearly_returns = {}
    for year in range(df.index.year.min(), df.index.year.max() + 1):
        year_data = df[df.index.year == year]
        if not year_data.empty:
            start_price = year_data.iloc[0]['Close']
            end_price = year_data.iloc[-1]['Close']
            yearly_return = (end_price - start_price) / start_price * 100
            yearly_returns[year] = yearly_return
    
    average_return = sum(yearly_returns.values()) / len(yearly_returns) if yearly_returns else 0
    return yearly_returns, average_return

def save_returns_to_csv(returns_data, average_return, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Year", "Return (%)"])
        for year, ret in returns_data.items():
            writer.writerow([year, ret])
        writer.writerow([])
        writer.writerow(["Average Annual Return", average_return])

def main():
    coins = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]  # Биткоин, Эфириум, и, например, Cardano
    start_time = datetime(2014, 1, 1)
    end_time = datetime.now()
    
    for coin in coins:
        data = get_historical_data(coin, "1d", start_time, end_time)
        filename = f"{coin}_daily_data.csv"
        save_to_csv(data, filename)
        print(f"Данные для {coin} сохранены в {filename}")
        
        returns_data, average_return = calculate_annual_returns(filename)
        returns_filename = f"{coin}_annual_returns.csv"
        save_returns_to_csv(returns_data, average_return, returns_filename)
        print(f"Доходность для {coin} сохранена в {returns_filename}")

if __name__ == "__main__":
    main()

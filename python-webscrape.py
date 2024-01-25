import yfinance as yf
import datetime
import random
import math
import pandas as pd
from termcolor import colored

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist

def apply_lambda_functions(data):
    # Lambda to calculate daily percentage change
    percentage_change = data.apply(lambda row: ((row['Close'] - row['Open']) / row['Open']) * 100, axis=1)

    # Lambda to find day with the highest volume
    highest_volume_day = data['Volume'].idxmax()

    return percentage_change, highest_volume_day

def math_operations(data):
    mean_close = data['Close'].mean()
    std_dev_close = data['Close'].std()
    max_close = data['Close'].max()
    min_close = data['Close'].min()
    # Find the dates for max and min closing prices
    date_max_close = data[data['Close'] == max_close].index[0]
    date_min_close = data[data['Close'] == min_close].index[0]

    return mean_close, std_dev_close, max_close, min_close, date_max_close, date_min_close

def trading_days(data):
    return len(data)

def latest_trading_date(data):
    return data.index[-1]

def random_number_generator(data):
    random_date = random.choice(data.index)
    random_price = data.loc[random_date, 'Close']
    return random_date, random_price

# Example Usage
ticker = 'AAPL'
stock_data = get_stock_data(ticker)

percentage_change, highest_volume_day = apply_lambda_functions(stock_data)
mean_close, std_dev_close, max_close, min_close, date_max_close, date_min_close = math_operations(stock_data)
trading_days_count = trading_days(stock_data)
last_trading_date = latest_trading_date(stock_data)
random_date, random_price = random_number_generator(stock_data)





print(colored(f"Stock Data for {ticker}:", 'blue'))
print(stock_data.head())

print(colored("\nDaily Percentage Change:", 'green'))
print(percentage_change.head())

print(colored(f"\nDay with Highest Volume: {highest_volume_day}", 'cyan'))
print(colored(f"Mean Closing Price: {mean_close}", 'red'))
print(colored(f"Standard Deviation of Closing Prices: {std_dev_close}", 'yellow'))
print(colored(f"Maximum Closing Price: {max_close} on {date_max_close}", 'magenta'))
print(colored(f"Minimum Closing Price: {min_close} on {date_min_close}", 'magenta'))
print(colored(f"Number of Trading Days: {trading_days_count}", 'cyan'))
print(colored(f"Most Recent Trading Date: {last_trading_date}", 'cyan'))
print(colored(f"Random Date: {random_date}, Random Closing Price: {random_price}", 'green'))


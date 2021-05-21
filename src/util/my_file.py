
from pathlib import Path
from os import listdir
from util.my_web import stock_database

"""
Handle file input/output, e.g.:
- storing stock data series into CSV files
- loading CSV files to python dictionaries
"""
########################################################################################
# Configuration
file_prefix="../trading_data/"
csv_delimiter = ","
########################################################################################


def store_csv(stock_name, date_series, price_series):
    filename = file_prefix + stockname_to_filename(stock_name) + ".csv"
    Path(file_prefix).mkdir(parents=True, exist_ok=True)

    with open(filename, "w") as file:
        # write csv header
        file.write("dates{}prices\n".format(csv_delimiter))
        # write csv rows
        for date, price in zip(date_series, price_series):
            file.write("{}{}{}\n".format(date, csv_delimiter, price))


def load_csv(stock_name):
    """
    Load CSV file and return data series
    :return: ([date], [price]) pair
    """
    filename = file_prefix + stockname_to_filename(stock_name) + ".csv"
    dates    = []
    prices   = []
    with open(filename, "r") as file:
        file.__next__()
        for line in file:
            date, price = line.strip().split(csv_delimiter)
            dates.append(date)
            prices.append(float(price))
    return dates, prices


def stored_stocks():
    """
    Return a list of csv file available
    """
    return [filename_to_stockname(file.split(".")[0]) for file in listdir(file_prefix)]


def print_stored_stocks():
    stocks = stored_stocks()
    for stock in stocks:
        print("{} - {}".format(stock, stock_database[stock]["name"]))

def stockname_to_filename(stock_name):
    return stock_name.replace(":", "_")


def filename_to_stockname(filename):
    return filename.replace("_", ":")
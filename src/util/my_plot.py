from matplotlib import pyplot as plt
import datetime as dt

def plot_values(*args):
    """
    When we plot price against dates
    :param args:    either (values) or (dates, values)
    """
    assert 1 <= len(args) <= 2

    if len(args) == 1:      # assume prices
        plt.plit(args[0])
    if len(args) == 2:      # assume dates, prices
        dates = [dt.datetime.strptime(d, '%Y-%m-%d') for d in args[0]]
        plt.plot(dates, args[1])

    plt.tight_layout()
    plt.show()


colors = ['b','g','c','m','y']

model_prices = []
stock_prices = []

def add_stock(stock_series):
    global stock_prices
    stock_prices = stock_series

def add_evaluation(model_series):
    model_prices.append(model_series)


def plot_all():
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("time")
    ax1.set_ylabel("stock price")
    ax1.plot(stock_prices, color="red")

    ax2 = ax1
    # ax2 = ax1.twinx()
    # ax2.set_ylabel("portfolio price", color="blue")
    for i, prices in enumerate(model_prices):
        ax2.plot(prices, color=colors[i])
    fig.tight_layout()
    plt.show()
from matplotlib import pyplot as plt
import datetime as dt


def plot_values(*args):
    """
    When we plot price against dates
    :param args:    either (values) or (dates, values)
    """
    assert 1 <= len(args) <= 2

    if len(args) == 1:  # assume prices
        plt.plit(args[0])
    if len(args) == 2:  # assume dates, prices
        dates = [dt.datetime.strptime(d, '%Y-%m-%d') for d in args[0]]
        plt.plot(dates, args[1])

    plt.tight_layout()
    plt.show()


colors = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
]
linewidth = .51
stock_prices = []
model_prices = []
model_names  = []


def add_stock(stock_series):
    global stock_prices
    stock_prices = stock_series


def add_evaluation(model_series, model_name):
    model_prices.append(model_series)
    model_names.append(model_name)


def plot_all():
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel("time")
    ax.set_ylabel("stock price")
    if stock_prices is not []:
        ax.plot(stock_prices, lw=linewidth, color="red")

    ax2 = ax
    # ax2 = ax1.twinx()
    # ax2.set_ylabel("portfolio price", color="blue")
    for i, prices in enumerate(model_prices):
        ax2.plot(prices, lw=linewidth, color=colors[i])
    fig.legend(["stock"] + model_names, loc=2)
    fig.tight_layout()
    plt.show()
    fig.savefig("../graphs/all.pdf")

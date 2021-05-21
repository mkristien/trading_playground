from matplotlib import pyplot as plt
import datetime as dt


def plot_values(*args):
    """
    When we plot price against dates
    :param args:    either (values) or (dates, values)
    """
    assert 1 <= len(args) <= 2

    if len(args) == 1:      # assume values
        plt.plit(args[0])
    if len(args) == 2:      # assume dates, values
        dates = [dt.datetime.strptime(d, '%Y-%m-%d') for d in args[0]]
        plt.plot(dates, args[1])

    plt.tight_layout()
    plt.show()

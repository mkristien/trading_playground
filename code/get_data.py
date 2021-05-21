#!/usr/bin/env python
import argparse
import util.my_web
import util.my_plot


class ShowOptionAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        util.my_web.print_available_stocks()
        exit(0)


parser = argparse.ArgumentParser(description="Get stock prices from the Internet")
parser.add_argument("-s", "--show", nargs=0, action=ShowOptionAction, help="Print available stock options")
parser.add_argument("-d", "--display", action="store_true", help="Plot fetched data")
parser.add_argument("stock", type=str, help="stock short name, as returned by --show")

if __name__ == "__main__":
    args = parser.parse_args()

    # make sure selected stock exist in our database
    assert args.stock in util.my_web.stock_database.keys(), "We do not know about this stock"

    date_series, value_series = util.my_web.fetch_data(args.stock)

    if args.display:
        util.my_plot.plot_values(date_series, value_series)

    pass

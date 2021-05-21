#!/usr/bin/env python
import argparse
import util.my_web
import util.my_plot
import util.my_file


class ShowOptionAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        util.my_file.print_stored_stocks()
        exit(0)


parser = argparse.ArgumentParser(description="Load stock data that are stored locally")
parser.add_argument("-s", "--show", nargs=0, action=ShowOptionAction, help="Print local stock data options")
parser.add_argument("stock", type=str, help="stock short name, as returned by --show")

if __name__ == "__main__":
    args = parser.parse_args()

    date_series, price_series = util.my_file.load_csv(args.stock)

    util.my_plot.plot_values(date_series, price_series)

    pass

#!/usr/bin/python
import util.my_web
import util.my_plot


if __name__ == "__main__":
    date_series, value_series = util.my_web.fetch_data()

    print("loaded", len(value_series), "data points")
    util.my_plot.plot_values(value_series)
    print(date_series)
    pass
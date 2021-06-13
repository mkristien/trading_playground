#!/usr/bin/env python
import argparse

import util.my_file
import util.my_plot

from predictor.regular_investment import RegularInvestment
from predictor.lin_regression import StartInvestment

##########################################################################################
# Configuration
initial_funds   = 1000

model_database = {
    "RegularInvestment": {
        "predictor": RegularInvestment,
        "description": "Invest in regular intervals, e.g. every week"
    },
    "StartInvestment": {
        "predictor": StartInvestment,
        "description": "Invest all funds at the beginning, watch it grow"
    }
}

class ShowStockAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        util.my_file.print_stored_stocks()
        exit(0)

class ShowModelAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        for name, value in model_database.items():
            print("{} - {}".format(name, value["description"]))
        exit(0)

parser = argparse.ArgumentParser(description="Get stock prices from the Internet")
parser.add_argument("-s", "--show-stocks", nargs=0, action=ShowStockAction, help="Print available stock options")
parser.add_argument("-m", "--show-models", nargs=0, action=ShowModelAction, help="Print available trading models")
parser.add_argument("-p", "--plot", action="store_true", help="Plot simulation history")
parser.add_argument("stock", type=str, help="stock short name, as returned by --show-stocks")
parser.add_argument("predictor", type=str, help="predictor name to use in the simulation, as returned by --show-models")

##########################################################################################
# Simulation
evaluation_history   = []
current_stock_amount = 0


def current_evaluation(stock_amount, stock_price):
    return stock_amount*stock_price


def create_model(model_name, simulation_time):
    return model_database[model_name]["predictor"](initial_funds, simulation_time)


def run_simulation(price_series, trading_model):
    global current_stock_amount
    step = 0
    for price in price_series:
        model.feed_price(price)

        # buy and sell
        buy  = trading_model.buy_amount()
        sell = trading_model.sell_amount()
        current_stock_amount += buy / price
        current_stock_amount -= sell/ price

        trading_model.sell(sell)
        trading_model.buy(buy)

        # update simulated portfolio value
        evaluation_history.append(current_evaluation(current_stock_amount, price))
        step += 1


if __name__ == "__main__":
    args = parser.parse_args()

    _, price_series = util.my_file.load_csv(args.stock)

    model = create_model(args.model, len(price_series))

    run_simulation(price_series, model)

    current_value = current_evaluation(current_stock_amount, price_series[-1])

    print("Final evaluation:", current_value)
    print("Initial vs final funds: {}, {} -> {}%".format(
        model.initial_funds,
        current_value+model.remaining_funds,
        ((current_value+model.remaining_funds-model.initial_funds)*100) / model.initial_funds
    ))

    if args.plot:
        util.my_plot.add_stock(price_series)
        util.my_plot.add_evaluation(evaluation_history)
        util.my_plot.plot_all()
    pass
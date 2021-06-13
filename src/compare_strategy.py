#!/usr/bin/env python
import argparse
import util.my_file
import util.my_plot

from strategy.just_buy import JustBuy
from strategy.just_buy import GradualBuy
from strategy.buy_when_going_up import BuyWhenGoingUp
from strategy.strategy_interface import NoInvesting

from predictor.lin_regression import LinearRegression
from predictor.constant import TheSameAsYesterday
from predictor.exponential_mean import ExponentialMean9, ExponentialMean99, ExponentialMean8


##########################################################################################
# Configuration
initial_funds = 1000.0
daily_deposit = 0.0

predictor_classes = [
    LinearRegression,
    TheSameAsYesterday,
    ExponentialMean8,
    ExponentialMean9,
    ExponentialMean99
]

strategy_classes = [
    NoInvesting,        # predictor irrelevant
    JustBuy,            # predictor irrelevant
    GradualBuy,         # predictor irrelevant
    BuyWhenGoingUp,
]

class ShowStockAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        util.my_file.print_stored_stocks()
        exit(0)


parser = argparse.ArgumentParser(description="Get stock prices from the Internet")
parser.add_argument("-s", "--show-stocks", nargs=0, action=ShowStockAction, help="Print available stock options")
parser.add_argument("stock", type=str, help="stock short name, as returned by --show-stocks")
parser.add_argument("-t", "--train", metavar='N', type=int, default=100, help="number of days to train predictor")

##########################################################################################
# Simulation
class StrategyRunner:
    def __init__(self, stock_name, train_period):
        _, self.prices    = util.my_file.load_csv(stock_name)
        self.train_period = train_period

        training_prices = self.prices[:self.train_period]
        # create strategy+predictor combination
        self.strategies = [
            NoInvesting(initial_funds, TheSameAsYesterday, training_prices),
            JustBuy(initial_funds, TheSameAsYesterday, training_prices),
            GradualBuy(initial_funds, TheSameAsYesterday, training_prices),
            BuyWhenGoingUp(initial_funds, LinearRegression, training_prices),
            BuyWhenGoingUp(initial_funds, TheSameAsYesterday, training_prices),
            BuyWhenGoingUp(initial_funds, ExponentialMean8, training_prices),
            BuyWhenGoingUp(initial_funds, ExponentialMean9, training_prices),
            BuyWhenGoingUp(initial_funds, ExponentialMean99, training_prices),
        ]

        # initialise all valuations
        self.values = []
        for strategy in self.strategies:
            self.values.append([strategy.total_value()])

    def run(self):
        simulation_prices = self.prices[self.train_period:]
        for price in simulation_prices:
            # perform strategy transactions and record valuation after each day
            for i, strategy in enumerate(self.strategies):
                strategy.buy()
                self.values[i].append(strategy.total_value())
                strategy.feed_price(price)
                strategy.deposit(daily_deposit)

        # update final day valuation
        final_valuations = []
        for i, strategy in enumerate(self.strategies):
            final_value = strategy.total_value()
            self.values[i].append(final_value)
            final_valuations.append(final_value)

        return final_valuations

    def print_data(self):
        for i, strategy in enumerate(self.strategies):
            util.my_plot.add_evaluation(self.values[i], str(strategy))

        util.my_plot.plot_all()

    def get_names(self):
        result = []
        for strategy in self.strategies:
            result.append(str(strategy))
        return result

if __name__ == "__main__":
    args = parser.parse_args()

    runner       = StrategyRunner(args.stock, args.train)
    final_values = runner.run()
    ratios = []
    for value in final_values:
        ratios.append(value/final_values[0])
    names = runner.get_names()

    for i in range(len(names)):
        print("{}\t{}\t{}".format(final_values[i], ratios[i], names[i]))


    # runner.print_data()

    pass
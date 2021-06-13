#!/usr/bin/env python
import argparse
import util.my_plot
import util.my_file

from predictor.lin_regression import LinearRegression
from predictor.star_to_end_price import StartToEndLine
from predictor.constant import TheSameAsYesterday
from predictor.exponential_mean import ExponentialMean9, ExponentialMean99, ExponentialMean8

predictor_classes = [
    LinearRegression,
    # StartToEndLine,   # this one is useless, almost the same as TheSameAsYesterday
    TheSameAsYesterday,
    ExponentialMean8,
    ExponentialMean9,
    ExponentialMean99
]


class PredictorRunner:
    true_prices      = []   # list of stock data prices
    predictor_prices = []   # list of list of predicted prices
    train_period     = 0

    def __init__(self, stock_name, train_period):
        _, self.true_prices = util.my_file.load_csv(stock_name)
        self.train_period = train_period

    def run(self):
        """
        Run stock prices through several predictor_classes, recording their prediction
        :return: [] list of prediction accuracies
        """
        # initialise predictor_classes, assume perfect prediction during training
        training_prices = self.true_prices[:self.train_period]
        self.predictors = []
        errors     = []
        for _, predictor in enumerate(predictor_classes):
            # create a predictor object
            self.predictors.append(predictor(training_prices))
            errors.append(0)
            # copy all true prices from training period
            self.predictor_prices.append([])
            for price in training_prices:
                self.predictor_prices[-1].append(price)

        # go through remaining prices and record predictions
        for price in self.true_prices[self.train_period:]:
            # make predictions and update predictors with the true price
            for i, predictor in enumerate(self.predictors):
                new_price = predictor.predicted_price()
                errors[i] += abs(new_price - price)

                self.predictor_prices[i].append(new_price)
                predictor.feed_price(price)

        return errors

    def print_data(self):
        util.my_plot.add_stock(self.true_prices)
        for i, predictor in enumerate(self.predictors):
            util.my_plot.add_evaluation(self.predictor_prices[i], str(predictor))

        util.my_plot.plot_all()





class ShowOptionAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        util.my_file.print_stored_stocks()
        exit(0)


parser = argparse.ArgumentParser(description="Pick stock data and run it through predictor_classes")
parser.add_argument("-s", "--show", nargs=0, action=ShowOptionAction, help="Print local stock data options")
parser.add_argument("stock", type=str, help="stock short name, as returned by --show")
parser.add_argument("-t", "--train", metavar='N', type=int, default=100, help="number of days to train predictor")

if __name__ == "__main__":
    args = parser.parse_args()

    runner = PredictorRunner(args.stock, args.train)
    errors = runner.run()
    print(errors)

    runner.print_data()

    pass

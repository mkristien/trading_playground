"""
A model is fed series of price data over time during the trading simulation.

A model should keep its internal state and reflect on it when new data arrives.
"""


class AbstractModel:
    initial_funds       = 0.0   # how much money can we spend
    remaining_funds     = 0.0
    projected_period    = 0   # how many investment days are we gonna see?
    def __init__(self, funds=1000.0, period=365):
        self.initial_funds    = funds
        self.remaining_funds  = funds
        self.projected_period = period

    def feed_price(self, price):
        raise NotImplementedError("Implement handling of new price data")

    def buy_amount(self):
        raise NotImplementedError("Model advices to buy more stock")

    def sell_amount(self):
        raise NotImplementedError("Model advices to sell stock")

    def should_hold(self):
        return self.buy_amount() + self.sell_amount() == 0.0

    def buy(self, amount):
        self.remaining_funds -= amount
        assert self.remaining_funds >= 0.0, "remaining funds lowered to {}".format(self.remaining_funds)

    def sell(self, amount):
        self.remaining_funds += amount

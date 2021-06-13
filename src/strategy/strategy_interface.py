
class AbstractStrategy:
    """
    Strategy uses a predictor model to "guess" the next day stock price
    and makes judgement on buy/sell in terms of money to be put into
    or taken out from a stock.

    Strategy also keeps track of available fund.
    Deposit and withdrawals should be supported at any time.
    """
    def __init__(self, initial_funds, predictor_class, prices):
        self.funds     = initial_funds
        self.stock     = 0
        self.predictor = predictor_class(prices)    # create predictor object
        self.price     = self.predictor.price_history[-1]

    def buy_amount(self):
        """
        How much should we money should we put into the stock.
        Funds are not adjusted just by asking this method.

        Negative amount means we are selling.
        :return: money value of suggesting stock buying
        """
        raise NotImplementedError("Implement buying stocks")

    def buy(self):
        """
        Actually modify funds by simulating putting money into the stock.

        Negative amount means we are selling stock, increasing available funds.
        """
        amount = self.buy_amount()
        price  = self.price
        if amount > 0:
            assert self.funds >= amount, "Not enough funds to buy , {} vs {} available". format(amount, self.funds)
        else:
            assert self.stock_value() >= abs(amount),\
                "Not enough stock to sell this much, {} vs {} stock value".format(abs(amount), self.stock_value(price))

        self.funds -= amount
        self.stock += amount / price

    def deposit(self, amount):
        """
        Increase available funds.

        Negative amounts means withdrawal
        """
        if amount < 0:
            assert self.funds >= amount, "Not enough funds to withdraw, {} vs {} available".format(amount, self.funds)
        self.funds += amount

    def feed_price(self, price):
        self.price = price
        self.predictor.feed_price(price)

    def __str__(self):
        raise NotImplementedError("Implement pretty printing of this strategy name")

    def fund_value(self):
        return self.funds

    def stock_value(self):
        return self.stock * self.price

    def total_value(self):
        return self.fund_value() + self.stock_value()


class NoInvesting(AbstractStrategy):
    def buy_amount(self):
        return 0.0

    def __str__(self):
        return "NoInvesting"
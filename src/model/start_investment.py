
from model.model_interface import AbstractModel


class StartInvestment(AbstractModel):
    invested = False

    def __init__(self, funds, period):
        super().__init__(funds, period)
        self.invested = False

    def feed_price(self, price):
        pass

    def buy_amount(self):
        if not self.invested:
            self.invested = True
            return self.initial_funds       # buy as much as you can at the beginning

        return 0.0

    def sell_amount(self):
        return 0.0

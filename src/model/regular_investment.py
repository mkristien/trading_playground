
from model.model_interface import AbstractModel


class RegularInvestment(AbstractModel):

    def __init__(self, funds, period, frequency=7):
        """
        :param frequency: how regularly should we buy stock, e.g. 7 -> every week
        """
        super().__init__(funds, period)
        self.frequency = frequency
        self.count     = frequency
        self.increment = self.initial_funds / (self.projected_period / frequency)

    def feed_price(self, price):
        pass

    def buy_amount(self):
        """
        Invest every time the frequency counter expires
        """
        self.count -= 1

        if self.count != 0:
            return 0.0

        self.count = self.frequency
        return self.increment

    def sell_amount(self):
        return 0.0

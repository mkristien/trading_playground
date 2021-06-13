from strategy.strategy_interface import AbstractStrategy


class JustBuy(AbstractStrategy):
    """
    Always buy using all available funds
    """
    def buy_amount(self):
        return self.funds

    def __str__(self):
        return "JustBuy"


class GradualBuy(AbstractStrategy):
    """
    Always buy using a percentage of available funds
    """
    def buy_amount(self):
        return self.funds * 0.02

    def __str__(self):
        return "GradualBuy"

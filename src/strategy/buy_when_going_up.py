from strategy.strategy_interface import AbstractStrategy


class BuyWhenGoingUp(AbstractStrategy):
    """
    Buy/Sell based on stock prediction using a percentage of value
    """
    def buy_amount(self):
        current_price   = self.price
        predicted_price = self.predictor.predicted_price()
        if predicted_price > current_price:
            return self.funds * 0.1
        else:
            return -self.stock_value() * 0.1

    def __str__(self):
        return "BuyWhenGoingUp_"+str(self.predictor)

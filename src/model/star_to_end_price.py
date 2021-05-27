from model.model_interface import AbstractModel


class StartToEndLine(AbstractModel):
    def __init__(self, price_history):
        super().__init__(price_history)

    def feed_price(self, price):
        self.price_history.append(price)

    def predicted_price(self):
        '''
        Calculate future price by drawing a straight line from the beginning to the end
        of the historical prices.
        Extrapolate the line to the next day price.
        '''
        price_difference_from_start = self.price_history[-1] - self.price_history[0]
        price_difference_per_day    = price_difference_from_start / len(self.price_history)
        tomorrow_price              = self.price_history[-1] + price_difference_per_day
        return tomorrow_price

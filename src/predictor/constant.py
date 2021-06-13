from predictor.model_interface import AbstractPredictor


class TheSameAsYesterday(AbstractPredictor):
    def __init__(self, price_history):
        super().__init__(price_history)

    def __str__(self):
        return "TheSameAsYesterday"

    def feed_price(self, price):
        self.price_history.append(price)

    def predicted_price(self):
        '''
        Guess the price will be the same as yesterday
        '''
        return self.price_history[-1]

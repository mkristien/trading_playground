"""
A model makes a future predictions of the price development.

During initialization, a price history is provided so that the model
can configure/train its internal state.
Then, "daily" price updates are provided, resulting in change
of the internal model state.

When queried, the model makes prediction about future price development
"""
class AbstractModel:
    price_history = []
    def __init__(self, price_history):
        '''
        Create a new model, initialize internal state based on historical price data
        :param price_history: a list of prices observed in the past
        '''
        # copy price history to local list
        for price in price_history:
            self.price_history.append(price)

    def feed_price(self, price):
        '''
        Update the model with a new daily price
        :param price: the new value of the stocks
        '''
        raise NotImplementedError("Implement handling of new price data")

    def predicted_price(self):
        '''
        Ask the model, what will be the tomorrow's price
        :return: (price, confidence)
        price       - predicted value of the stocks tomorrow
        confidence  -
        '''
        raise NotImplementedError("Implement making future price prediction")

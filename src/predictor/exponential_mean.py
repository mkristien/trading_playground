from predictor.model_interface import AbstractPredictor


class ExponentialMeanParametric(AbstractPredictor):
    """
    Compute running exponential mean as:
    mean = mean * L + new_value * (1-L)
    for alpha parameter L being 0 < L < 0

    The alpha parameter determines how fast should the mean adapt to new prices.
    High values of Alpha is slower to respond to changes
    """
    def __init__(self, price_history, alpha):
        super().__init__(price_history)
        self.alpha = alpha
        self.mean  = 0

        # set initial mean as arithmetic average
        sum = 0
        for price in price_history:
            sum += price
        self.mean = sum / len(price_history)

    def __str__(self):
        return "ExpMean alpha={}".format(self.alpha)

    def feed_price(self, price):
        self.price_history.append(price)
        self.mean = self.mean * self.alpha + price * (1 - self.alpha)

    def predicted_price(self):
        """
        Assume stock price will regress to the running exponential mean
        """
        return self.mean


class ExponentialMean9(ExponentialMeanParametric):
    def __init__(self, price_history):
        super().__init__(price_history, 0.9)


class ExponentialMean8(ExponentialMeanParametric):
    def __init__(self, price_history):
        super().__init__(price_history, 0.8)

class ExponentialMean99(ExponentialMeanParametric):
    def __init__(self, price_history):
        super().__init__(price_history, 0.99)


from predictor.model_interface import AbstractPredictor

from scipy import stats


class LinearRegression(AbstractPredictor):
    def __init__(self, price_history):
        super().__init__(price_history)
        self.slope, self.intercept, _, _, _ = stats.linregress(
            range(len(self.price_history)),
            self.price_history
        )

    def __str__(self):
        return "LinearRegression"

    def feed_price(self, price):
        self.price_history.append(price)
        self.slope, self.intercept, _, _, _ = stats.linregress(
            range(len(self.price_history)),
            self.price_history
        )

    def predicted_price(self):
        """
        Assume trained linear regression will continue to tomorrow
        """
        return self.slope * len(self.price_history) + self.intercept


if __name__ == "__main__":
    model = LinearRegression([0, 1, 2, 3, 4])
    print(model.predicted_price())  # should be 5
    model.feed_price(0)
    print(model.predicted_price())  # should be 2.6666

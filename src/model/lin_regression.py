from model.model_interface import AbstractModel

from scipy import stats
import numpy as np
# >>> x = np.random.random(10)
# >>> y = np.random.random(10)
# >>> slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

class LinearRegression(AbstractModel):
    slope       = 0
    intercept   = 0
    def __init__(self, price_history):
        super().__init__(price_history)
        self.slope, self.intercept, _, _, _ = stats.linregress(
            range(len(self.price_history)),
            self.price_history
        )

    def feed_price(self, price):
        self.price_history.append(price)
        self.slope, self.intercept, _, _, _ = stats.linregress(
            range(len(self.price_history)),
            self.price_history
        )

    def predicted_price(self):
        '''
        Assume trained linear regression will continue to tomorrow
        '''
        return self.slope * len(self.price_history) + self.intercept


if __name__ == "__main__":
    model = LinearRegression([0,1,2,3,4])
    print(model.predicted_price())  # should be 5
    model.feed_price(0)
    print(model.predicted_price())  # should be 2.6666


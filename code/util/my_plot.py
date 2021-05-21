from matplotlib import pyplot as plt

# When we plot price agains dates
def plot_values(dates, values):
    plt.plot(dates, values)
    plt.tight_layout()
    plt.show()

def plot_values(values):
    plt.plot(range(len(values)), values)
    plt.tight_layout()
    plt.show()
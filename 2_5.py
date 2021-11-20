import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return np.cos(x)


def deriv(x, delta_x=0.0001):
    return (function(x + delta_x) - function(x)) / delta_x


def deriv_f(x):
    return -np.sin(x)


data = np.linspace(-15, 15, 300)

fig, ax = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(13, 5))

ax[0].plot(data, deriv(data), label="deriv", color="darkviolet")
ax[0].legend(loc="upper left")

ax[1].plot(data, deriv_f(data), label="deriv_function", color="red")
ax[1].legend(loc="upper left")
plt.show()

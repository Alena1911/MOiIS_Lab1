import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10000)
f_y = x - (x ** 3) / 6 + (x ** 5) / 120 - (x ** 7) / 5040
g_y = np.sin(x)

plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.grid()
plt.plot(x, f_y, label="f(x)")
plt.plot(x, g_y, label="g(x)")
plt.legend(loc="upper left")
plt.xlim(-5, 5)
plt.show()

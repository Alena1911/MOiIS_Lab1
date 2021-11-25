from random import randint
import numpy as np


x = np.random.randint(low=-300, high=300, size=500)
w = np.random.randint(low=-300, high=300, size=500)
b = randint(-300, 300)
print("Вывод: ", np.dot(x, w) + b)

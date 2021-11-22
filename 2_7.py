import numpy as np
import matplotlib.pyplot as plt

vec = []
v, q = 3, 10
for i in range(v, q):
    inc = 0
    points = np.random.random(size=(900, i))
    for point in points:
        if 1 >= sum([x ** 2 for x in point]):
            inc += 1
    vec.append(inc / 1000)
fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 8))
ax.plot(range(v, q), vec, 100)
ax.set_ylim(0, 0.8)
ax.set_xlim(v, q)
plt.show()

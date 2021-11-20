import numpy as np
import matplotlib.pyplot as plt


def transformation_plot(points, matrix):
    x = points[:, 0]
    y = points[:, 1]

    color = x * y
    ax[0].scatter(x, y, 10, c=color)
    trans_points = np.dot(points, matrix.T)
    trans_x = trans_points[:, 0]
    trans_y = trans_points[:, 1]
    ax[1].scatter(trans_x, trans_y, 10, c=color)


fig, ax = plt.subplots(1, 2, figsize=(15, 8))
transformation_plot(np.random.random(size=(1000, 2)), np.array([[3, 5], [6, 4]]))
plt.show()

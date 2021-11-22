import numpy as np
import matplotlib.pyplot as plt


# Скользящее среднее
def running_mean(x, N):
    out = np.zeros_like(x, dtype=np.float64)
    dim_len = x.shape[0]
    for i in range(dim_len):
        if N % 2 == 0:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 2
        else:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 1
        a = max(0, a)
        b = min(dim_len, b)
        # вычисляем среднее
        out[i] = np.mean(x[a:b])
    return out


# Скользящая медиана
def running_median(x, N):
    out = np.zeros_like(x, dtype=np.float64)
    dim_len = x.shape[0]
    for i in range(dim_len):
        if N % 2 == 0:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 2
        else:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 1
        a = max(0, a)
        b = min(dim_len, b)
        # вычисляем медиану
        out[i] = np.median(x[a:b])
    return out


t = np.linspace(1, 30, 1000)
noise = np.random.normal(0, 1, 1000)
final_signal = t + noise
y_signal = np.sin(final_signal)
plt.subplot(3, 1, 1)
plt.plot(t, y_signal)

plt.subplot(3, 1, 2)
plt.plot(t, running_mean(y_signal, 3))

plt.subplot(3, 1, 3)
plt.plot(t, running_median(y_signal, 3))

plt.show()

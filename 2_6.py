import numpy as np


V = [np.array([5, 3]), np.array([4, 10])]
Q = np.array([2, 10])

Len90vec = 0
Len30vec = 0

l_q = np.sqrt(np.sum(Q**2))
for v in V:
    l_v = np.sqrt(np.sum(v**2))
    if np.degrees(np.arccos(np.dot(v, Q.reshape(-1, 1)) / (l_v * l_q))) < 90:
        Len90vec += 1
    if np.degrees(np.arccos(np.dot(v, Q.reshape(-1, 1)) / (l_v * l_q))) < 30:
        Len30vec += 1
    print(f'90 градусов: {Len90vec / len(V)}\n'
          f'30 градусов: {Len30vec / len(V)}')

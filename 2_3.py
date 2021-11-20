import matplotlib.pyplot as plt
r = float(input("r="))
circle1 = plt.Circle((0, 0), r, color='darkviolet', fill=False)
ax=plt.gca()
ax.add_patch(circle1)
plt.axis('scaled')
plt.grid()
plt.show()

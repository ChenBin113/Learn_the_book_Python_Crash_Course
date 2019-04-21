import matplotlib.pyplot as plt

x_values = [i for i in range(1, 5)]
y_values = [j ** 3 for j in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='none')

x_values = [i for i in range(1, 5000)]
y_values = [j ** 3 for j in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='none')

plt.show()

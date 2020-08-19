import matplotlib.pyplot as plt

x_values = list(range(0,101))
y_values = [x ** 3 for x in x_values]

plt.title('Graph for : y=x^3',fontsize = 24)
plt.xlabel('x-axis', fontsize = 16)
plt.ylabel('y-axis', fontsize = 16)

plt.axis([0,100,0,1000000])
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, edgecolor = 'none', s = 10 )
plt.show()

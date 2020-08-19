import matplotlib.pyplot as plt

value = list(range(1,101))
squares_value = [num**2 for num in value]
#chart title
plt.title('Square Numbers', fontsize = 24)
#axis label
plt.xlabel('values', fontsize = 16)
plt.ylabel('squares of value', fontsize = 16)

plt.plot(value,squares_value,c=(1,0.4,1),linewidth = 2)
plt.show()

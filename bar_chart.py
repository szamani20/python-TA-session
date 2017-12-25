import matplotlib.pyplot as plt

# Data
x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]

# Second Data
x2 = [1, 3, 5, 7, 9]
y2 = [2, 4, 6, 8, 10]

# Create BarChart
plt.bar(x, y, label='Bar Chart', color='cyan')

# Create second BarChart
plt.bar(x2, y2, label='Bar Chart 2', color='purple')

# Label for x axis
plt.xlabel('X')

# Label for y axis
plt.ylabel('Y')

# title of graph
plt.title('Good Graph\nSubtitle')

# Add legend
plt.legend()

# show graph
plt.show()

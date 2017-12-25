import matplotlib.pyplot as plt

# Data
x = [1, 2, 3]
y = [4, 5, 6]

# second data
x2 = [1, 2, 3]
y2 = [10, 12, 14]

# Create Plot
plt.plot(x, y, label='First Line')

# Create second plot
plt.plot(x2, y2, label='Second Line')

# Label for x axis
plt.xlabel('X Label')

# Label for y axis
plt.ylabel('Y Label')

# title of graph
plt.title('Good Graph\nSubtitle')

# Add legend (for second data)
plt.legend()

# show graph
plt.show()

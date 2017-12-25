import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 1, 7, 7, 2, 9, 2, 3]

# Create plot
plt.scatter(x, y, label='scat', color='k', marker='*', s=1000)

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

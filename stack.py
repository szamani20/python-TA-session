import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7]
sleeping = [6, 7, 7, 8, 7, 9, 9]
eating = [2, 3, 2, 3, 2, 4, 4]
working = [8, 8, 8, 7, 7, 6, 6]
studying = [1, 1, 1, 1, 2, 2, 3]

# Create plot
plt.stackplot(days, sleeping, eating, working, studying,
              colors=['c', 'r', 'm', 'y'],
              labels=['Sleep', 'Eat', 'Work', 'Study'])

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

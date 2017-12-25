import matplotlib.pyplot as plt

# Data
slices = [9, 4, 6, 3]

# Create plot
plt.pie(slices, colors=['c', 'r', 'y', 'm'],
        labels=['Sleep', 'Eat', 'Work', 'Study'],
        startangle=90,
        shadow=True,
        explode=(0, 0, 0, 0.1),
        autopct='%1.1f%%')

# title of graph
plt.title('Good Graph\nSubtitle')

# show graph
plt.show()

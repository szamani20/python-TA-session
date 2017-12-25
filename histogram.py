import matplotlib.pyplot as plt

age_distribution = [22, 33, 44, 55, 66, 77, 88, 99, 23, 44, 55, 66, 77, 88, 99, 23, 34, 45, 56, 67, 78, 55, 66, 77, 88,
                    99, 23, 34, 45, 56, 67, 78, 89, 100]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

# Create histogram
plt.hist(age_distribution, bins, histtype='bar', rwidth=0.8)

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

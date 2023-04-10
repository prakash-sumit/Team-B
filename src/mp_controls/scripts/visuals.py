import matplotlib.pyplot as plt

# set the size of the figure
fig = plt.figure(figsize=(4, 6))

# create a subplot
ax = fig.add_subplot(1, 1, 1)

# plot the points
ax.plot(x, y, 'o')

# set the limits of the x and y axes
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

# show the grid
ax.grid(True)

# show the plot
plt.show()

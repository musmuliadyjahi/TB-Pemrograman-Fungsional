from matplotlib import pyplot as plt
x = [0, 1, 3]
y = [0, 2, 3]

# create a line chart, years on x-axis, gdp on y-axis
plt.arrow(x[0], y[0], 1, 2, head_width=0.1,
          head_length=0.2, length_includes_head=True)
plt.arrow(x[1], y[1], 2, 1, head_width=0.1,
          head_length=0.2, length_includes_head=True)
plt.arrow(x[2], y[2], -x[2], -y[2])

# add a title
plt.title("Chart Garis")
# add a label to the y-axis
plt.ylim(-0.5, 3.5)
plt.xlim(-1, 4)
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()

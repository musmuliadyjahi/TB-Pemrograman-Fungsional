import matplotlib.pyplot as plt
import string

alpha = string.ascii_lowercase
y = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
x, y1, y2 = [], [], []

for i in range(len(y)):
    y1.append(y[i]*1.5)
    y2.append(y[i]*-1)
    x.append(alpha[i])

plt.scatter(x, y, s=100,  marker='^')
plt.scatter(x, y1, s=150, marker='1')
plt.scatter(x, y2, s=200, marker='p')
plt.show()

import matplotlib.pyplot as plt
import string

alpha = string.ascii_lowercase
y = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
x, y1, y2, y3 = [], [], [], []

for i in range(len(y)):
    y1.append(y[i]*1.5)
    y2.append(y[i]*-1)
    y3.append(y[i]*-1.5)
    x.append(alpha[i])

plt.plot(x, y, linestyle='-.')
plt.plot(x, y1, linestyle=':')
plt.plot(x, y2, linestyle='--')
plt.plot(x, y3, linestyle='-')
plt.grid(True)
plt.show()

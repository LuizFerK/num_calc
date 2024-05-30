import matplotlib.pyplot as plt
import numpy as np
import math

title = 'Euler'
n = 5
y = [0]
min_x = 0
max_x = 1

# ------------------------

euler_number = math.exp(1)
x = []

def f(x):
  return math.cos(x)

def exact(x):
  return math.sin(x)

h = (max_x - min_x) / (n - 1)

for i in range(n - 1):
  x.append(h * i)
  y.append(y[i] + h * f(h * i))

x.append(max_x)

# Generate x values from -10 to 10
x_values = np.linspace(-10, 10, 400)
# Calculate y values using the function y
y_values = list(map(exact, x_values))

# Plot config
plt.figure(figsize=(12, 12))
plt.plot(x_values, y_values, label='exact')
plt.scatter(x, y, label='f(x)')
plt.title(title)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
max_x = 3
min_x = -3
max_y = 3
min_y = -3
plt.axis([min_x, max_x, min_y, max_y])
plt.xticks(np.arange(min_x, max_x, 1))
plt.yticks(np.arange(min_y, max_y, 1))
plt.show()

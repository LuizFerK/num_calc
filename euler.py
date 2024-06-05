import matplotlib.pyplot as plt
import numpy as np
import math

# Entradas
n = 5
y = [1]
min_x = 0
max_x = 1

# e
euler_number = math.exp(1)
x = []

# y'
def f(x):
  return euler_number ** x + 1

# y
def exact(x):
  return euler_number ** x + x

# ------------------------

# Intervalo
h = (max_x - min_x) / (n - 1)

for i in range(n - 1):
  x.append(h * i)
  y.append(y[i] + h * f(h * i))

x.append(max_x)

# Gera valores x de -10 to 10
x_values = np.linspace(-10, 10, 400)

# Calcula valores y usando a função y
y_values = list(map(exact, x_values))

# Plot config
plt.figure(figsize=(12, 12))
plt.plot(x_values, y_values, label='exact')
plt.scatter(x, y, label='f(x)')
plt.title('Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
max_x = 2
min_x = -0.5
max_y = 5
min_y = 0
plt.axis([min_x, max_x, min_y, max_y])
plt.xticks(np.arange(min_x, max_x, 0.25))
plt.yticks(np.arange(min_y, max_y, 1))
plt.show()

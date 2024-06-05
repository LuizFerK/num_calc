import matplotlib.pyplot as plt
import numpy as np

# Entradas
x = 30

# ------------------------------------

# Produto de Lagrange
def li(p, i, x, x_points):
  r = 1

  for j in range(p + 1):
    if (i == j):
      continue
    r *= (x - x_points[j]) / (x_points[i] - x_points[j])

  return r

# Somatório de Lagrange
def lagrange(p, x, x_points, y_points):
  r = 0

  for i in range(p + 1):
    r += y_points[i] * li(p, i, x, x_points)

  return r

# C15
x_points = [69.2, 34.9, 23.4, 17.7, 14.3, 12, 10.4, 9.2, 8.2, 7.5, 6.8, 6.3, 5.9, 5.5, 5.2, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.8, 3.8, 3.7, 3.5, 3.4, 3.3, 3.2, 3.2, 3.1, 3, 2.9, 2.9, 2.8, 2.7, 2.6, 2.6]
y_points = [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.438, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.628, 0.64, 0.68, 0.72, 0.76, 0.772]

# Definições de variáveis
x_prev = x_points[0]
x_next = x_points[0]
x_next2 = x_points[0]
y_prev = 0
y_next = 0
y_next2 = 0

# Encontrando valores vizinhos de x e f(x)
for idx, xi in enumerate(x_points):
  if (xi > x):
    x_prev = x_points[idx + 1]
    x_next = xi
    x_next2 = x_points[idx - 1]
    y_prev = y_points[idx + 1]
    y_next = y_points[idx]
    y_next2 = y_points[idx - 1]

# Calculando f(x) usando Lagrange
y1 = lagrange(1, x, [x_prev, x_next], [y_prev, y_next])
y2 = lagrange(2, x, [x_prev, x_next, x_next2], [y_prev, y_next, y_next2])

print(y1, y2)

# Plot config
plt.figure(figsize=(12, 12))
plt.scatter(x_points, y_points, label='pontos C15')
plt.scatter([x], [y1], label="valor interpolado P1")
plt.scatter([x], [y2], label="valor interpolado P2")
plt.plot(x_points, y_points, label='p1(x) = x**2 + x + 2')
plt.title('Interpolação')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
max_x = 40
min_x = 10
max_y = 0.1
min_y = 0
plt.axis([min_x, max_x, min_y, max_y])
plt.xticks(np.arange(min_x, max_x, 3))
plt.yticks(np.arange(min_y, max_y, 0.01))
plt.show()

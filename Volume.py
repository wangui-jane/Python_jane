import numpy as np

# Set up the grid
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
dx = dy = x[1] - x[0]

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Approximate volume using Riemann sum
volume = np.sum(Z) * dx * dy
print("Volume under surface z = x^2 + y^2 over [0,1]x[0,1] is:", volume)

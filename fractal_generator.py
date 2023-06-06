import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
	# Create an array of complex coordinates
	x = np.linspace(x_min, x_max, width)
	y = np.linspace(y_min, y_max, height)
	c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

	# Create an array to store the iteration counts
	fractal = np.zeros(c.shape, dtype=int)

	# Iterate the fractal equation
	z = np.zeros(c.shape, dtype=complex)
	for i in range(max_iter):
		mask = np.abs(z) < 2.0
		z[mask] = z[mask] * z[mask] + c[mask]
		fractal += mask

	return fractal

def generate_burning_ship(width, height, x_min, x_max, y_min, y_max, max_iter):
	# Create an array of complex coordinates
	x = np.linspace(x_min, x_max, width)
	y = np.linspace(y_min, y_max, height)
	c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

	# Create an array to store the iteration counts
	fractal = np.zeros(c.shape, dtype=int)

	# Iterate the fractal equation
	z = np.zeros(c.shape, dtype=complex)
	for i in range(max_iter):
		mask = np.abs(z) < 2.0
		z[mask] = np.abs(z[mask].real) + 1j * np.abs(z[mask].imag)
		z[mask] = z[mask] * z[mask] + c[mask]
		fractal += mask

	return fractal


def generate_julia(width, height, x_min, x_max, y_min, y_max, max_iter, c):
	# Create an array of complex coordinates
	x = np.linspace(x_min, x_max, width)
	y = np.linspace(y_min, y_max, height)
	z = x[:, np.newaxis] + 1j * y[np.newaxis, :]

	# Create an array to store the iteration counts
	fractal = np.zeros(z.shape, dtype=int)

	# Iterate the fractal equation
	for i in range(max_iter):
		mask = np.abs(z) < 2.0
		z[mask] = z[mask] * z[mask] + c
		fractal += mask

	return fractal


def generate_sierpinski(width, height, num_iterations):
	# Create an empty array to store the fractal
	fractal = np.zeros((height, width), dtype=int)

	# Set the initial point to the center of the array
	x, y = width // 2, height // 2

	# Define the three vertices of the triangle
	vertices = [(0, height - 1), (width - 1, height - 1), (width // 2, 0)]

	# Iterate the fractal construction
	for _ in range(num_iterations):
		# Randomly select one of the triangle vertices
		vx, vy = vertices[np.random.randint(0, 3)]

		# Calculate the midpoint between the current point and the selected vertex
		x = (x + vx) // 2
		y = (y + vy) // 2

		# Set the pixel at the midpoint as "on"
		fractal[y, x] = 1

	return fractal


def plot_fractal(fractal):
	plt.imshow(fractal.T, cmap='hot', extent=[-2, 1, -1.5, 1.5])
	plt.xlabel("Re")
	plt.ylabel("Im")
	plt.title("Fractal")
	plt.show()
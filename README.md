# Fractal Generator

This module provides functions to generate and plot various fractals using NumPy and Matplotlib libraries. The following fractals are currently supported:

- Mandelbrot Set
- Burning Ship
- Julia Set
- Sierpinski Triangle

## Installation

To use this module, you need to have Python 3 installed along with the NumPy and Matplotlib libraries. You can install the required libraries using pip:

```shell
pip install numpy matplotlib
```

## Usage

Import the module and use the provided functions to generate and plot fractals.

```python
import numpy as np
import matplotlib.pyplot as plt
import fractal_generator

# Generate a Mandelbrot fractal
fractal = fractal_generator.generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Generate a Burning Ship fractal
fractal = fractal_generator.generate_burning_ship(width, height, x_min, x_max, y_min, y_max, max_iter)

# Generate a Julia fractal
fractal = fractal_generator.generate_julia(width, height, x_min, x_max, y_min, y_max, max_iter, c)

# Generate a Sierpinski Triangle fractal
fractal = fractal_generator.generate_sierpinski(width, height, num_iterations)

# Plot the fractal
fractal_generator.plot_fractal(fractal)
```

Replace the function arguments with appropriate values for your desired fractal.

## Fractal Functions

### generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

Generates a Mandelbrot fractal.

- `width`: Width of the fractal image in pixels.
- `height`: Height of the fractal image in pixels.
- `x_min`: Minimum value of the x-axis.
- `x_max`: Maximum value of the x-axis.
- `y_min`: Minimum value of the y-axis.
- `y_max`: Maximum value of the y-axis.
- `max_iter`: Maximum number of iterations to compute the fractal.

Returns the generated fractal as a NumPy array.

### generate_burning_ship(width, height, x_min, x_max, y_min, y_max, max_iter)

Generates a Burning Ship fractal.

- `width`: Width of the fractal image in pixels.
- `height`: Height of the fractal image in pixels.
- `x_min`: Minimum value of the x-axis.
- `x_max`: Maximum value of the x-axis.
- `y_min`: Minimum value of the y-axis.
- `y_max`: Maximum value of the y-axis.
- `max_iter`: Maximum number of iterations to compute the fractal.

Returns the generated fractal as a NumPy array.

### generate_julia(width, height, x_min, x_max, y_min, y_max, max_iter, c)

Generates a Julia fractal.

- `width`: Width of the fractal image in pixels.
- `height`: Height of the fractal image in pixels.
- `x_min`: Minimum value of the x-axis.
- `x_max`: Maximum value of the x-axis.
- `y_min`: Minimum value of the y-axis.
- `y_max`: Maximum value of the y-axis.
- `max_iter`: Maximum number of iterations to compute the fractal.
- `c`: Complex constant for the Julia set.

Returns the generated fractal as a NumPy array.

### generate_sierpinski(width, height, num_iterations)

Generates a Sierpinski Triangle fractal.

- `width`: Width of the fractal image in pixels.
- `height`: Height of

 the fractal image in pixels.
- `num_iterations`: Number of iterations to construct the fractal.

Returns the generated fractal as a NumPy array.

### plot_fractal(fractal)

Plots the given fractal using Matplotlib.

- `fractal`: Fractal image as a NumPy array.

## License

This module is licensed under the [MIT License](LICENSE).

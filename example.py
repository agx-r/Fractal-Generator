from fractal_generator import generate_burning_ship, plot_fractal

width = 800
height = 600
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 1000

fractal = generate_burning_ship(width, height, x_min, x_max, y_min, y_max, max_iter)
plot_fractal(fractal)
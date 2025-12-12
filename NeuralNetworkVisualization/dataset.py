import numpy as np

def generate_data(func_name="x2", n_points=100):
    x = np.linspace(-4, 4, n_points).reshape(-1, 1)

    if func_name == "x2":
        y = x**2
    elif func_name == "x3":
        y = x**3
    elif func_name == "sin":
        y = np.sin(x)
    else:
        raise ValueError("Unknown function name")

    # Normalize y to prevent gradient explosion
    y_mean = np.mean(y)
    y_std = np.std(y)
    y_normalized = (y - y_mean) / (y_std + 1e-8)
    
    return x, y_normalized

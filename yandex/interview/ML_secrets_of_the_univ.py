import sys
import numpy as np
from scipy.optimize import curve_fit

lines = sys.stdin.read().splitlines()
n = int(lines[0])
x_data, y_data = [], []
for line in lines[1:]:
    x, y = map(float, line.strip().split())
    x_data.append(x)
    y_data.append(y)

x_data = np.array(x_data)
y_data = np.array(y_data)

def model(x, a, b, c, d):
    return a * np.tan(x) + (b * np.sin(x) + c * np.cos(x))**2 + d * np.sqrt(x)

initial_guess = [1, 1, 1, 1]
params, _ = curve_fit(model, x_data, y_data, p0=initial_guess)

print(f"{params[0]:.2f} {params[1]:.2f} {params[2]:.2f} {params[3]:.2f}")

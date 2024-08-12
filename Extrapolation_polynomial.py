#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:37:10 2024

@author: fateyhabegum
"""
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1896,1900,1904,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020])
ys = np.array([12,11,11,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,10.20,10,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85,9.69,9.63,9.81,9.80])

# Quadratic, cubic, and hexic polynomial models
quadratic_model = np.poly1d(np.polyfit(xs, ys, 2))
cubic_model = np.poly1d(np.polyfit(xs, ys, 3))
hexic_model = np.poly1d(np.polyfit(xs, ys, 6))

# Predict winning times for the year 2024
predicted_time_quadratic = quadratic_model(2024)
predicted_time_cubic = cubic_model(2024)
predicted_time_hexic = hexic_model(2024)

# Print predicted winning times
print(f"Predicted winning time for 2024 (Quadratic model): {predicted_time_quadratic:.2f} seconds")
print(f"Predicted winning time for 2024 (Cubic model): {predicted_time_cubic:.2f} seconds")
print(f"Predicted winning time for 2024 (Hexic model): {predicted_time_hexic:.2f} seconds")

# Plotting
polyline = np.linspace(min(xs), 2024, 1000)
plt.plot(polyline, quadratic_model(polyline), label="Quadratic model", color="orange")
plt.plot(polyline, cubic_model(polyline), label="Cubic model", color="purple")
plt.plot(polyline, hexic_model(polyline), label="Hexic model", color="magenta")
plt.scatter(xs, ys)
plt.scatter(2024, predicted_time_quadratic, label="Extrapolated point (Quadratic)")
plt.scatter(2024, predicted_time_cubic, color="purple", label="Extrapolated point (Cubic)")
plt.scatter(2024, predicted_time_hexic, color="magenta", label="Extrapolated point (Hexic)")
plt.plot(xs, ys, label="Men's 100m winning time")
plt.xlabel('Year', fontsize=14)
plt.ylabel('Winning time (s)', fontsize=14)
plt.title("Men's Olympic 100m Winning Times from 1896 to 2024")
plt.legend(fontsize=11, frameon=False)
plt.xticks(rotation=90.0, fontsize=12.0)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.grid()

### TO PLOT THE SEPERATE POLYNOMIALS, JUST COMMENT OUT THE ONES NOT DESIRED ###
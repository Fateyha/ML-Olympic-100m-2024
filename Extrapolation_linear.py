#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:13:06 2024

@author: fateyhabegum
"""

from scipy import interpolate
from statistics import mean
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

xs = np.array([1896,1900,1904,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020])
ys = np.array([12,11,11,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,10.20,10,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85,9.69,9.63,9.81,9.80])

def best_fit_slope_and_intercept(xs,ys):
    m = (((np.mean(xs) * np.mean(ys)) - np.mean(xs*ys)) / ((np.mean(xs)**2) - np.mean(xs**2)))
    c = np.mean(ys) - m*np.mean(xs)

    return m,c

def squared_error(ys_original, ys_line):
    return sum((ys_line - ys_original)**2)

def r_squared(ys_original,ys_line):
      y_mean_line = [np.mean(ys_original) for y in ys_original]
      squared_error_regression = squared_error(ys_original,ys_line)
      squared_error_y_mean = squared_error(ys_original,y_mean_line)
      return 1 - (squared_error_regression/squared_error_y_mean)

m,c=best_fit_slope_and_intercept(xs,ys)

regression_line = [(m*x)+c for x in xs]
print(f"This is the value of the gradient: {m}")

result = r_squared(ys, regression_line)
print(f"This is the R-squared value: {result}")

# Fit a linear model
linear_model = np.poly1d(np.polyfit(xs,ys,1)) 

# Extrapolate for the year 2024
predicted_time_2024 = linear_model(2024)
print(f"Predicted winning time for 2024: {predicted_time_2024:.2f} seconds")

# Plotting
polyline = np.linspace(min(xs),2024, 1000)
extrapolated_val = linear_model(polyline)


plt.title("Men\'s olympic 100m winning times from 1896 to 2024")
plt.scatter([2024], [predicted_time_2024], color='orangered', label='Extrapolated point (2024)')
plt.scatter(xs,ys)
plt.plot(xs,ys,label='Men\'s 100m winning time')
plt.plot(xs,regression_line,label='Line of best fit',color="red")
plt.xlabel('Year',fontsize=14)
plt.ylabel('Winning time (s)',fontsize=14)
plt.legend(fontsize=11,frameon=False)
plt.xticks(rotation=90.0,fontsize=12.0)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.grid()
plt.show()

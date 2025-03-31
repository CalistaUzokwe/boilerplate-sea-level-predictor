import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (1880-2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_extended = np.arange(df['Year'].min(), 2051)
    y_extended = slope * x_extended + intercept
    plt.plot(x_extended, y_extended, color='red', label='Line of Best Fit (1880-2050)')

    # Second line of best fit (2000-2050)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_extended_recent = np.arange(2000, 2051)
    y_extended_recent = slope_recent * x_extended_recent + intercept_recent
    plt.plot(x_extended_recent, y_extended_recent, color='green', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel("Year") # Remove indentation here
    plt.ylabel("Sea Level (inches)") # Remove indentation here
    plt.title("Rise in Sea Level") # Remove indentation here
    plt.legend() # Remove indentation here

    plt.savefig('sea_level_plot.png')
    plt.show()  # Add this right before return plt.gca()
    return plt.gca()

draw_plot()
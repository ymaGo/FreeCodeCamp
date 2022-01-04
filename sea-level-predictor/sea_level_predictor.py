import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result_1 = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    x_1 = [i for i in range(1880,2051)]
    y1_fit = [result_1.slope * i + result_1.intercept for i in x_1]
    plt.plot(x_1, y1_fit)

    # Create second line of best fit
    df_2=df[df.Year>=2000]
    result_2 = linregress(df_2.Year, df_2["CSIRO Adjusted Sea Level"])
    x_2 = [i for i in range(2000,2051)]
    y2_fit = [result_2.slope * i + result_2.intercept for i in x_2]
    plt.plot(x_2, y2_fit)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
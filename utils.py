import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error

def get_dataframe(data):
    data = data['result'][0]['values']

    df = pd.DataFrame(data, columns=['date', 'kpi'])
    df['date'] = pd.to_datetime(df['date'], unit='s')
    set(df['date'].dt.date)
    df['kpi'] = pd.to_numeric(df['kpi'], errors='ignore')
    return df


def plot(df):
    plt.figure(figsize=(10, 10))
    plt.plot(df['date'], df['kpi'], 'blue', label='stat')

    plt.ylim(0, 100)
    plt.xlabel('Date')
    plt.ylabel('KPI')
    plt.title('KPI stat')
    plt.legend();
    plt.show()


def plot_moving_average(series, window, plot_intervals=False, scale=1.96):
    rolling_mean = series.rolling(window=window).mean()

    plt.figure(figsize=(17, 8))
    plt.title('Moving average\n window size = {}'.format(window))
    plt.plot(rolling_mean, 'g', label='Rolling mean trend')

    # Plot confidence intervals for smoothed values
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bound, 'r--', label='Upper bound / Lower bound')
        plt.plot(lower_bound, 'r--')

    plt.plot(series[window:], label='Actual values')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()


def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
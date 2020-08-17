import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

from scipy.optimize import minimize
import statsmodels.tsa.api as smt
import statsmodels.api as sm

from tqdm import tqdm_notebook

from itertools import product



from prometheus_client import PrometheusClient
from utils import plot, get_dataframe, plot_moving_average


client = PrometheusClient('http://localhost:9090')
query = 'sum by(instance) (100 - 100 * (sum by(instance) (node_filesystem_avail_bytes) / sum by(instance) (node_filesystem_size_bytes))) '
query = '(100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100))'
instance = '192.168.33.133:9100'
ts_data = client.range_query(query, instance, step=60, days=2)  # returns PrometheusData object
print(ts_data)
"""
ts = ts_data.timeseries[0] # returns a TimeSeries object

json_data = ts.as_json()

dataframe = ts.as_pandas_dataframe()
"""

dataframe = get_dataframe(ts_data)
#plot(dataframe)


plot_moving_average(dataframe.kpi, 3, plot_intervals=True)






print('hola')

import csv
from time import sleep
import plotly.express as px
import numpy as np


def plot_graph(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Coffee in ml', y = 'Sleep in hours')
        fig.show()

def get_data_src(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for i in csvReader:
            coffee.append(float(i['Coffee in ml']))
            sleep.append(float(i['Sleep in hours']))
    return {'x':coffee, 'y':sleep}

def find_correlation(data_src):
    correlation = np.corrcoef(data_src['x'],data_src['y'])
    print('The correlation between the coffee drank and the amount of sleep is {0}.'.format(str(correlation)))

def main():
    data_path = 'csv_files/coffee.csv'
    data_src = get_data_src(data_path)
    find_correlation(data_src)
    plot_graph(data_path)
main()
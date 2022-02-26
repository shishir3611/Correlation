import csv
import plotly.express as px
import numpy as np


def plot_graph(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Days Present', y = 'Marks In Percentage')
        fig.show()

def get_data_src(data_path):
    days = []
    marks = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for i in csvReader:
            days.append(float(i['Days Present']))
            marks.append(float(i['Marks In Percentage']))
    return {'x':days, 'y':marks}

def find_correlation(data_src):
    correlation = np.corrcoef(data_src['x'],data_src['y'])
    print('The correlation between the days on which they were present and the marks they got is {0}.'.format(str(correlation)))

def main():
    data_path = 'csv_files/marks.csv'
    data_src = get_data_src(data_path)
    find_correlation(data_src)
    plot_graph(data_path)
main()
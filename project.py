
import plotly.express as px
import csv
import numpy as np


def getDataSource(dataPath):
    week = []
    coffee = []

    with open(dataPath) as f:
        reader = csv.DictReader(f)


        for row in reader:
            week.append(float(row['week']))
            coffee.append(float(row['Coffee in ml']))

    return{'x':week, 'y':coffee}

def findCorrelation(getDataSource):
    corr = np.corrcoef(getDataSource['x'], getDataSource['y'])
    print(corr[0,1])

def plot(dataPath):
 
    with open (dataPath) as f:
        reader = csv.DictReader(f)
        
        fig = px.scatter(reader, x = "week", y = "Coffee in ml")
        fig.show()


def setup():
    dataPath = 'Data4.csv'
    ds = getDataSource(dataPath)
    plot(dataPath)
    findCorrelation(dataPath)

setup()












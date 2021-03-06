import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    Marks_In_Percentage = []
    Days_Present = []
    with open("C:\\Users\\Dhairya\\Desktop\\python\\c 106\\project\\c 106 project\\data.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return{"x": Marks_In_Percentage,"y": Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between Marks In Percentage vs Days Present:-  \n---> ", correlation[0,1])

def setup():
    data_path = "C:\\Users\\Dhairya\\Desktop\\python\\c 106\\project\\c 106 project\\data.csv" 
    
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

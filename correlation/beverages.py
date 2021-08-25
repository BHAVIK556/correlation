# import plotly.express as px
import csv
import numpy as np

    # get the data from csv and load it in an array in float format


def getDatasource(data_path):
    ice_cream_sales=[]
    cold_drink_sales=[]
    with open(data_path) as csv_file:
     reader=csv.DictReader(csv_file)
     # fig= px.scatter(reader,x="Temperature",y="Ice-cream Sales( ₹ )")
     #fig.show()

    for row in csv_file:
        ice_cream_sales.append(float(row["Temperature"]))
        cold_drink_sales.append(float(row["Ice-cream Sales( ₹ )"]))
       
    return { "x": ice_cream_sales,"y":cold_drink_sales} 

def findCorrelation(datasource):
     # find out correlation coefficient ,using function corrcoef()
       correlation= np.corrcoef(datasource["x"],datasource["y"])
       print("correlation between temperature vs ice cream sales :-  \n-->",correlation[0,1])

def setup():
    data_path= "./SA2.csv"

    datasource=getDatasource(data_path)
    findCorrelation(datasource)
    
    

setup()

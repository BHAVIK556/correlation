#import plotly_express as px
import csv
import numpy as np

# to compare the tv watched/week
#with open ("./SA3.csv") as csv_file:
    #reader=csv.DictReader(csv_file)
    #fig= px.histogram(reader,x="Size of TV",y="\tAverage time spent watching TV in a week (hours)")
    #fig.show()
    # correlation 0


    
def getDatasource(data_path):
    Size_of_TV=[]
    Average_time_spent=[]
    with open(data_path) as csv_file:
     reader=csv.DictReader(csv_file)
     # fig= px.scatter(reader,x="Temperature",y="Ice-cream Sales( ₹ )")
     #fig.show()

    for row in csv_file:
        Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
        Size_of_TV.append(float(row["Size of TV"]))
       
    return { "x":Size_of_TV ,"y":Average_time_spent} 

def findCorrelation(datasource):
     # find out correlation coefficient ,using function corrcoef()
       correlation= np.corrcoef(datasource["x"],datasource["y"])
       print("correlation between size of the tv and average time spent watching :-  \n-->",correlation[0,1])

def setup():
    data_path= "./SA3.csv"

    datasource=getDatasource(data_path)
    findCorrelation(datasource)
    
    

setup()

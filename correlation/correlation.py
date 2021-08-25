import plotly.express as px
import csv

with open ("./SA1.csv") as csv_file:
    reader=csv.DictReader(csv_file)
    fig= px.histogram(reader,x="Coffee in ml",y="sleep in hours",color="week")
    fig.show()
import plotly_express as px
import csv
import numpy as np

#  to compare the tv watched/week
with open ("./SA4.csv") as csv_file:
    reader=csv.DictReader(csv_file)
    fig= px.histogram(reader,x="Roll No",y="Marks In Percentage",color="Days Present")
    fig.show()
    # correlation 0


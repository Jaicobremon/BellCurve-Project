#Importing all modules
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.express as px

#Reading the csv file
df = pd.read_csv("AverageRatingMobile.csv")

#Creating the figure
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=True)

#Showing the figure
fig.show()

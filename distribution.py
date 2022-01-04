import pandas as pd 

df = pd.read_csv("data.csv")
import plotly.figure_factory as fg
fig = fg.create_distplot([df["Height(Inches)"].to_list()],["height"],show_hist=False)
fig.show()
import pandas as pd
import plotly_express as px
df = pd.read_csv("mobiledata.csv")
import plotly.figure_factory as fg
fig = fg.create_distplot([df["Avg Rating"].to_list()],["Average rating"],show_hist=False)
fig.show()
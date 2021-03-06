import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('project.csv')
figure = ff.create_distplot([df['Avg Rating'].tolist()],['Rating'],show_hist=False)
figure.show()
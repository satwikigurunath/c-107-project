import pandas as pa
import csv
import plotly.express as px

data = pa.read_csv("data 2.csv")
print(data.groupby("student_id")["attempt"].mean())

fig = px.scatter(data, x="student_id", y="level", color="attempt", size="attempt")
fig.show()
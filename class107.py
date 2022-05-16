import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
df=pd.read_csv('D:\project\class107\data.csv')

run=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
#print(run)
fig=px.scatter(run,x='student_id',y='level', size='attempt')
fig.show()


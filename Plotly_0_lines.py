import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
from plotly import graph_objs as go
import dash_vtk
import json
import numpy as np
from collections import deque



# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)


#------------------------------------------------------------------------------
app=dash.Dash(__name__)

with open("C:\\Dropbox\\00_TOMAS\\00_PC\\00_Projects\\Plotlling\\panels.json") as data:
    read_json=json.load(data)

#level= (read_json['L_1'])

#print (read_json)

fig1 = go.Figure()


listx=[0,5,0]
listy=[5,5,5]
listz=[0,0,5]
#fig1.add_trace(go.mesh3d(x=listx))
fig1.add_trace(go.Scatter3d(x=listx,y=listy,z=listz, mode='lines',line=dict(color='green',width=2)))
fig1.add_trace(go.Scatter3d(x=[listx[0],listx[-1]],y=[listy[0],listy[-1]],z=[listz[0],listz[-1]], mode='lines',line=dict(color='green',width=2)))
fig1.show()
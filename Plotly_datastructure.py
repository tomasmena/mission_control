
import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import plotly
from plotly import graph_objs as go
import json
from collections import deque
import numpy as np

#------------------------------------------------------------------------------
app=dash.Dash(__name__)
#----------------------------------------------------------------
# Import and Clean the data


with open("panels.json") as data:
    read_json=json.load(data)

listx,listy,listz=[],[],[]

for indexl,level in enumerate(read_json):
    listx.append([])  
    listy.append([])  
    listz.append([])  
    for indexp,panel in enumerate(read_json[level]):
        listx[indexl].append([])
        listy[indexl].append([])
        listz[indexl].append([])
         
        for indexpt,p in enumerate(read_json[level][panel]):
            listx[indexl][indexp].append(p[0])
            listy[indexl][indexp].append(p[1])
            listz[indexl][indexp].append(p[2])

with open("midpoints.json") as data:
    points=json.load(data)

labels=[]

for i,j in enumerate(points):
    # labels.append(j)
    # labels.append([])
    
    for k,l in enumerate(points[j]):
        labels.append(str(j+" "+l))
        # if (type(labels[i])) == list:
        #     labels[i].append(l)

# print (read_json["L_0"]["P_#0"])
# print (np.transpose(read_json["L_0"]["P_#0"])[0])

with open("inclinations.json") as data:
    inclinations=json.load(data)

# print (inclinations)

for i in inclinations:
    print(i)

print (inclinations["L_1"])
#l_p=str(inclinations[0])+str(inclinations[0][0])

app.layout= dash_table.DataTable(

    id='panel_data',
    columns=[{"name":'Level+Panel_Number',"id":"L+P"},{"name":'Inclination',"id":'inc'}],
    data=[{'L+P':'L_1 P_#0','inc':inclinations['L_1']['P_#0']}]
)
if __name__ == '__main__':
    app.run_server(debug=True,port=8000)


# ------------------------------------------------------------------------------------

# App Layout

# app.layout=html.Div([

#     html.H1 ("SCHUECO ANALYSIS VIEWER", style={'text-align':'center'}),dcc.Interval(
#             id='interval-component',
#             interval=10*1000, # in milliseconds
#             n_intervals=0),

#     # dcc.Dropdown(id="slct_data",
#     #             options=[
#     #                 {"label":"Level Organization","value":0},
#     #                 {"label":"Inclinations", "value":0},
#     #                 {"label":"Internal Angles", "value":0},
#     #                 {"label": "Neighbouring Angles", "value":0}],
#     #                 multi=False,
#     #                 value=0,
#     #                 style={'width':"40%"}
#     #                 ),
        
#     html.Div(id='output_container',children=[]),
#     html.Br(),


#     dcc.Graph(id='geometry_analysis',figure={})
# ])

# ----------------------------------------------------------------

# # Connect the plotly graphs with Dash Components 

"""
fig1 = go.Figure()
for index1,item in enumerate(listx):
    
    for index2, item2 in enumerate(item):
        clslinex=[item2[-1],item2[0]]
        clsliney=[listy[index1][index2][-1],listy[index1][index2][0]]
        clslinez=[listz[index1][index2][-1],listz[index1][index2][0]]
        
        fig1.add_trace(go.Mesh3d(x=item2,y=listy[index1][index2],z=listz[index1][index2], color="gray", opacity=0.65,i=[0],j=[1],k=[2]))
        fig1.add_trace(go.Scatter3d(x=item2,y=listy[index1][index2],z=listz[index1][index2],mode='lines',line=dict(color='green',width=2),showlegend=False))
        fig1.add_trace(go.Scatter3d(x=clslinex,y=clsliney,z=clslinez,mode='lines',line=dict(color='green',width=2),showlegend=False))


fig1.update_layout(
    scene = dict(
        xaxis = dict(showgrid=False,zeroline=False,visible=False,),
                    yaxis = dict(showgrid=False,zeroline=False,visible=False,),  
                    zaxis = dict(showgrid=False,zeroline=False,visible=True,),),
    #width=700,
    margin=dict(r=20, l=10, b=10, t=10))



fig1.show()

# #------------------------------------------------------------------------

#     #--------------------------------------------

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)
"""
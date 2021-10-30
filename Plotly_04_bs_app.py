
import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly
from plotly import graph_objs as go
import json
import numpy as np


# Import and Clean the data --------------------------------------------------------------

# Panels ######

with open("panels.json") as data:
    read_json=json.load(data)

listx=[]
listy=[]
listz=[]

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


# Points Inclinations ######

with open("midpoints.json") as data:
    read_points=json.load(data)


points_lx=[]
points_ly=[]
points_lz=[]
tags=[]

for index, level  in enumerate(read_points):
    points_lx.append([])
    points_ly.append([])
    points_lz.append([])
    for indexp, panelp in enumerate(read_points[level]):
        points_lx[index].append(read_points[level][panelp][0])
        points_ly[index].append(read_points[level][panelp][1])
        points_lz[index].append(read_points[level][panelp][2])


labels=[]

for i,j in enumerate(read_points):
    labels.append([])
    for k,l in enumerate(read_points[j]):
        labels[i].append(str(j+" "+l))
        
#print (labels)
trixp= listx[3][30]
triyp= listy[3][30]
trizp= listz[3][30]

with open("inclinations.json") as data:
    inclinations=json.load(data)

# ----------------------------------------------------------------
# App with dash_bootstrap_components

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX],
                    meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale=1.0'}]
                    )
app.title= "Schüco Analysis Viewer"
# ------------------------------------------------------------------
# App Layout with dash_bootstrap_components
app.layout= dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Shüco Viewer", 
                        className='text-center bg-dark text-light mt-4 display-4 text-capitalize font-weight-bolder'),
                        width=10)
    ],justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="slct_data",
                options=[
                    {"label":"Level Organization","value":0},
                    {"label":"Inclinations", "value":1},
                    {"label":"Internal Angles", "value":2},
                    {"label": "Neighbouring Angles", "value":3}],
                    multi=False,
                    value=0,
                    style={'width':"60%"}
                    ),
            dcc.Graph(id='geometry_analysis',figure={},clickData=None , hoverData=None, clear_on_unhover=True)
                        
            ],width={'size':6, 'order':1},class_name='d-*-block bg-secondary shadow-sm'),

        dbc.Col([
            dcc.Graph(id='panel',figure={}),
            dcc.Graph(id='table',figure={})
            ],width={'size':4, 'order':2},class_name='shadow' )
        ],justify='center',class_name='h-50')
    
],fluid=False)



# ----------------------------------------------------------------

# # Connect the plotly graphs with Dash Components 

### 
@app.callback(Output(component_id='geometry_analysis', component_property='figure'),
    #  Output(component_id='panel', component_property='figure')],
    Input(component_id='slct_data', component_property='value'))

def update_graph(option_slctd):


    fig1 = go.Figure()

    for index1,item in enumerate(listx):
        
        for index2, item2 in enumerate(item):
            clslinex=[item2[-1],item2[0]]
            clsliney=[listy[index1][index2][-1],listy[index1][index2][0]]
            clslinez=[listz[index1][index2][-1],listz[index1][index2][0]]
            
            fig1.add_trace(go.Mesh3d(x=item2,
                                    y=listy[index1][index2],
                                    z=listz[index1][index2],
                                    color="gray",
                                    opacity=0.65,
                                    i=[0],
                                    j=[1],
                                    k=[2],
                                    hoverinfo='skip',
                                    ))
            
            
            
    fig1.update_layout(
        scene = dict(
            xaxis = dict(showgrid=False,zeroline=False,visible=False,),
                        yaxis = dict(showgrid=False,zeroline=False,visible=False,),  
                        zaxis = dict(showgrid=False,zeroline=False,visible=True,),),
        #width=700,
        height=450,
        margin=dict(r=20, l=10, b=10, t=10))

    # PAnel graph
    
    if option_slctd == 0:
        for index1, item1 in enumerate(points_lx):
            fig1.add_trace(go.Scatter3d(
                x=item1,
                y=points_ly[index1],
                z=points_lz[index1],
                mode='markers',
                marker=dict(color="green", opacity=0.70),
                text=labels[index1],
                hoverinfo='text'))
            
                #fig1.update_traces(text=labels[index1])
    

    camera = dict(
            eye=dict(x=-2.5, y=-0.3, z=0.05) )


    fig1.update_layout(scene_camera=camera)
    
    return fig1 

 
#### Hovering on panels

@app.callback(
    Output(component_id='panel', component_property='figure'),
    Output(component_id='table', component_property='figure'),
    Input(component_id='geometry_analysis',component_property='hoverData'),
    Input(component_id='geometry_analysis',component_property='clickData')
) 

def update_side_graph(hov_Data,clk_data):

    # print (clk_data)
    # print (hov_Data)
    fig2=go.Figure()
    fig3=go.Figure()
    ctx=dash.callback_context
    #hpanel=np.transpose(read_json[(((hov_Data["points"][0]["text"]).split())[0])][(((hov_Data["points"][0]["text"]).split())[1])])
    #clpanel=np.transpose(read_json[(((clk_data["points"][0]["text"]).split())[0])][(((clk_data["points"][0]["text"]).split())[1])])
    #print (hov_Data)
    if  hov_Data is None:
        fig2.update(data=[go.Mesh3d(
                    x=[0,0,0],
                    y=[0,0,0],
                    z=[0,0,0],
                    color='blue',
                    opacity=0.7,
                    )])
        #print(hov_Data)

    else:
        hpanel=np.transpose(read_json[(((hov_Data["points"][0]["text"]).split())[0])][(((hov_Data["points"][0]["text"]).split())[1])])

        fig2.update(data=[go.Mesh3d(
                    x=hpanel[0],
                    y=hpanel[1],
                    z=hpanel[2],
                    color='gray',
                    opacity=0.5,
                    
                    )])
        
        #print(hov_Data)
    #print (clk_data)
    if  clk_data is None:

        fig2.update()
        
    else:
        clpanel=np.transpose(read_json[(((clk_data["points"][0]["text"]).split())[0])][(((clk_data["points"][0]["text"]).split())[1])])
        fig2.update(data=[go.Mesh3d(
                    x=clpanel[0],
                    y=clpanel[1],
                    z=clpanel[2],
                    color='green',
                    opacity=0.7,
                    
                    )])
        fig3=go.Figure(data=[go.Table(header=dict(values=['Levels','Inclinations']))])
        
                
    fig2.update_layout(

        scene = dict(
            xaxis = dict(showgrid=False,zeroline=False,visible=False),
                        yaxis = dict(showgrid=False,zeroline=False,visible=False),  
                        zaxis = dict(showgrid=False,zeroline=False,visible=True)),
        
        
        
        margin=dict(r=20, l=10, b=10, t=10),
        scene_aspectmode='data',
        height=300
            
        #scene_aspectratio=dict(x=0.5,y=0.5,z=2)
        )

    camera = dict(
            eye=dict(x=-5, y=-5, z=0.3) )


    fig2.update_layout(scene_camera=camera)
    
    
    return fig2,fig3

#fig1.show()

# #------------------------------------------------------------------------

#     #--------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

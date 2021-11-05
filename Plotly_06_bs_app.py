import os
from compas.datastructures import Mesh
import dash
from dash import dash_table
from dash import dcc
# from dash import html
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly
from plotly import graph_objs as go
import json
import numpy as np
import pandas as pd

# Import and Clean the data --------------------------------------------------------------

# Panels ######

with open("Plotlling\\panels.json") as data:
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

with open("Plotlling\\midpoints.json") as data:
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

with open("Plotlling\\inclinations.json") as data:
    inclinations=json.load(data)


here = os.path.dirname(__file__)
mesh = Mesh.from_json(os.path.join(here, 'mesh.json'))
# ----------------------------------------------------------------
# App with dash_bootstrap_components

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX],
                    meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale=1.0'}]
                    )
app.title= "Schüco Viewer"
# ------------------------------------------------------------------


# App Layout with dash_bootstrap_components

# ----------------
# TAB Geometry 
#-----------------
graph_card= dbc.Card(dbc.CardBody([html.H6("Facade Geometry"),dcc.Dropdown(id= "slct_data",
                options=[
                    {"label":"Level Organization","value":0},
                    {"label":"Inclinations", "value":1},
                    {"label":"Internal Angles", "value":2},
                    {"label": "Neighbouring Angles", "value":3}],
                    multi=False,
                    value=0,
                    style={'width':"70%"}
                    ),
                    dcc.Graph(id='geometry_analysis',figure={},clickData=None , hoverData=None, clear_on_unhover=True)
                ]))

graph_card_2= dbc.Card(dbc.CardBody([html.H6("Panel"),dcc.Graph(id='panel',figure={})]),style={'height':'70%'}) 

table_card_3=dbc.Card(dbc.CardBody([html.H6("Panel Information"),
                                  dash_table.DataTable(id='table',
                                columns=[],
                                data=[],
                                style_cell={'padding': '2px'},
                                style_header={
                                        'backgroundColor': 'white',
                                        'border': '1px solid black',
                                        'fontWeight': 'bold',
                                        'textAlign':'left',
                                        'font_size':'12px',
                                        'font_case':'lower'
                                        }
    
                                    )
                                    ]),style={'height':'30%'})

#----------------------------------------------------
# TAB BIM
#----------

graph_card_1_t1=dbc.Card(
    dbc.CardBody(
        [html.Iframe(src="https://speckle.xyz/embed?stream=b991906712&commit=b9291c5698", height= 300, width=500 )]
        ),style={'height':'70vh', 'width':'6'}) 


## ----------------------------------------------------

## --PDF Tabs

PDF_0 =dbc.Card(
    dbc.CardBody(html.ObjectEl(data="assets\\Ucw value1.pdf",height=450, width=450),style={'height':'450','width':'6'}))
PDF_1 =dbc.Card(
    dbc.CardBody(html.ObjectEl(data="assets\\Ucw value2.pdf",height=450, width=450),style={'height':'700','width':'6'}))
PDF_2=dbc.Card(
    dbc.CardBody(html.ObjectEl(data="assets\\UcwUw_20.02.2019.pdf",height=450, width=450),style={'height':'700','width':'6'}))


PDFtabs= dbc.Tabs(
    [ dbc.Tab(PDF_0,label="Ucw value1"),
    dbc.Tab(PDF_1,label="Ucw value2"),
    dbc.Tab(PDF_2,label="Ucw Uw")
    ])

# --------------------------------------------------


tab0_content=html.Div([dbc.Row(html.H5("Geometry Analysis",className='mt-3 display-9 text-uppercase align-right text-secondary bg-secondary text-center', style={'float':'left'})),
            dbc.Row([
                dbc.Col([graph_card],width={'size':7, 'order':1},className='d-*-block'),
                dbc.Col([
                    graph_card_2,table_card_3
                    ],width={'size':5, 'order':2},align='top',md=5 )
                ],justify='center',className='d-*-block bg-light')])
    
tab1_content= dbc.Row([
        dbc.Col([graph_card_1_t1],className='d-*-block bg-secondary shadow-sm'),
        dbc.Col([PDFtabs],className='d-*-block bg-secondary shadow-sm')
        ],justify='center',style={'height':'600'})

tab2_content=dbc.Row([
        dbc.Col(html.ObjectEl(data="assets\\210709_21061966_Quantity_list_Only_Demo.pdf",height=450, width=700),style={'height':'450','width':'10'})],
        justify='center',style={'height':'600'})


tabs= dbc.Tabs(
    [
        dbc.Tab(tab0_content, label= 'Geometry'),
        dbc.Tab(tab1_content , label= 'BIM'),
        dbc.Tab(label= 'Statics'),
        dbc.Tab( tab2_content, label= 'Costs')

    ])


# ----------------------------------------------------------------

app.layout= dbc.Container([
    
    dbc.Row([
        dbc.Col(html.Div([html.Img(src="assets\\schueco_logo.PNG", height=20 , style={'float':'left' , 'display':'flex','position':'absolute','top':'35%','left':'1.5%'}),html.H1("Schüco Viewer", 
        className='text-center bg-light text-dark mt-4 display-6 font-weight-bolder', style={'align': 'center', 'border-style':'none' })]
        ,style={'align-content': 'center', 'position':'relative', 'border-bottom':'double'}),
        width=12    )],justify='center'), 
        dbc.Row([
        dbc.Col(dbc.CardHeader([tabs]), width={'size':12})
    ],justify='center')

    ])
 
# ----------------------------------------------------------------
# CALLBACKS
# # Connect the plotly graphs with Dash Components 

@app.callback(Output(component_id='geometry_analysis', component_property='figure'),
    #  Output(component_id='panel', component_property='figure')],
    Input(component_id='slct_data', component_property='value'))

def update_graph(option_slctd):


    fig1 = go.Figure()

    vertices, faces = mesh.to_vertices_and_faces()
    edges = [[mesh.vertex_coordinates(u), mesh.vertex_coordinates(v)] for u,v in mesh.edges()]
    line_marker = dict(color='rgb(0,0,0)', width=1.5)
    lines = []
    x, y, z = [], [],  []
    for u, v in edges:
        x.extend([u[0], v[0], [None]])
        y.extend([u[1], v[1], [None]])
        z.extend([u[2], v[2], [None]])

    lines = [go.Scatter3d(x=x, y=y, z=z, mode='lines', line=line_marker,hoverinfo='skip')]
    triangles = []
    for face in faces:
        triangles.append(face[:3])
        if len(face) == 4:
            triangles.append([face[2], face[3], face[0]])
    
    i = [v[0] for v in triangles]
    j = [v[1] for v in triangles]
    k = [v[2] for v in triangles]

    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]


    data = []
    faces = [go.Mesh3d(x=x,
                        y=y,
                        z=z,
                        i=i,
                        j=j,
                        k=k,
                        opacity=1.,
                        # contour={'show':True},
                        # vertexcolor=vcolor,
                        colorbar_title='Amplitude',
                        colorbar_thickness=10,
                        colorscale= 'agsunset', # 'viridis'
                        # intensity=intensity_,
                        intensitymode='cell',
                        showscale=True,
                        hoverinfo='skip'
            )]
    
    data.extend(lines)
    data.extend(faces)
    
    fig1  = go.Figure(data=data)
            
            
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
    Output(component_id='table',component_property='columns'),
    Output(component_id='table',component_property='data'), 
    Input(component_id='geometry_analysis',component_property='hoverData'),
    Input(component_id='geometry_analysis',component_property='clickData')
    ) 

def update_side_graph(hov_Data,clk_data):

    # print (clk_data)
    # print (hov_Data)
    fig2=go.Figure()
    column=[]
    data=[]
    df=[]
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

        column=[{"name":'Level+Panel_Number',"id":"L+P"},
                                            {"name":'Inclination',"id":'inc'},
                                            {"name":"Ia_a", "id":"Ia_a"},
                                            {"name":"Ia_b", "id":"Ia_b"},
                                             {"name":"Ia_b", "id":"Ia_c"}]
        
        panelnumber=[(clk_data["points"][0]["text"])]
        inc=inclinations[(((clk_data["points"][0]["text"]).split())[0])][(((clk_data["points"][0]["text"]).split())[1])]
        
        data=[{'L+P':panelnumber[0],'inc':np.round(inc[0],3)}]

        df=pd.DataFrame(data)

        data=df.to_dict('records')
        print (data)
                
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
    
    
    return fig2,column,data

#fig1.show()

# #------------------------------------------------------------------------

#     #--------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

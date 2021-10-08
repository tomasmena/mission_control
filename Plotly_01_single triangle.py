
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
from plotly import graph_objs as go
import json
from collections import deque




# Import and Clean the data

# Panels ######

with open("C:\\Users\\menatj\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\Schueco_Computation_Geometry\\Schueco_Computation_Geometry\\panels.json") as data:
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



trixp= listx[3][30]
triyp= listy[3][30]
trizp= listz[3][30]


fig=go.Figure(data=[go.Mesh3d(
                x=trixp,
                y=triyp,
                z=trizp,
                color='blue',
                opacity=0.7,


)])

fig.update_layout(
        scene = dict(
            xaxis = dict(showgrid=False,zeroline=False,visible=False),
                        yaxis = dict(showgrid=False,zeroline=False,visible=False),  
                        zaxis = dict(showgrid=False,zeroline=False,visible=True)),
        width=700,
        
        
        margin=dict(r=20, l=10, b=10, t=10),
        scene_aspectmode='data',
            
        #scene_aspectratio=dict(x=0.5,y=0.5,z=2)
        )



camera = dict(
    eye=dict(x=-5, y=-5, z=0.3) )


fig.update_layout(scene_camera=camera)
fig.show()


# Points Inclinations ######

with open("C:\\Users\\menatj\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\Schueco_Computation_Geometry\\Schueco_Computation_Geometry\\midpoints.json") as data:
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

# ------------------------------------------------------------------------------------

# App Layout
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Roboto:wght@400;700&display=swap"
        "family=Space+Mono:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

#------------------------------------------------------------------------------

"""

app=dash.Dash(__name__,external_stylesheets=external_stylesheets )
app.title= "Schüco Analysis Viewer"
#----------------------------------------------------------------
app.layout =html.Div([

    html.H1 ("SCHÜCO ANALYSIS VIEWER", style={'text-align':'center'}),

    dcc.Dropdown(id="slct_data",
                options=[
                    {"label":"Level Organization","value":0},
                    {"label":"Inclinations", "value":1},
                    {"label":"Internal Angles", "value":0},
                    {"label": "Neighbouring Angles", "value":0}],
                    multi=False,
                    value=0,
                    style={'width':"40%"}
                    ),
        
    html.Div(id='output_container',children=[]),
    html.Br(),
    html.Div(id='single_triangle', figure={}
    
            # children=[
            #     html.Table(
            #         html.Tbody([
                    
            #             html.Td(
            #                 dcc.Graph(id='geometry_analysis',figure={})
            #             ),
            #             html.Td(
            #                 dcc.Graph(id='geometry_analysis2',figure={})
            #             )

            #         ])
                    

            #     )
        # html.Div(
        #     children=[
        #         dcc.Graph(id='geometry_analysis',figure={}), 
        #     ],
        #     className="card"
        # ),
        # html.Div(
        #     children=[
                
        #         dcc.Graph(id='geometry_analysis2',figure={})
                
                
        #     ],
        #     className="card"
        # )
    ])

        
])
"""
# ----------------------------------------------------------------

# # Connect the plotly graphs with Dash Components 
"""
@app.callback(
     Output(component_id='geometry_analysis', component_property='figure'),
     #Output(component_id='geometry_analysis2', component_property='figure')],
    Input(component_id='slct_data', component_property='value'))



def update_graph(option_slctd):
    print (option_slctd)
    print (type(option_slctd))

    #container="The year chosen by the user was __ {}".format(option_slctd)


    
    print (listx[0][0])
    
    
    #fig1.add_trace(go.Mesh3d(x=item2,y=listy[index1][index2],z=listz[index1][index2], color="gray", opacity=0.65,i=[0],j=[1],k=[2]))
    # fig1.add_trace(go.Scatter3d(x=item2,y=listy[index1][index2],z=listz[index1][index2],mode='lines',line=dict(color='green',width=2),showlegend=False))
    # fig1.add_trace(go.Scatter3d(x=clslinex,y=clsliney,z=clslinez,mode='lines',line=dict(color='green',width=2),showlegend=False))


    

    fig1.update_layout(
        scene = dict(
            xaxis = dict(showgrid=False,zeroline=False,visible=False,),
                        yaxis = dict(showgrid=False,zeroline=False,visible=False,),  
                        zaxis = dict(showgrid=False,zeroline=False,visible=True,),),
        #width=700,
        margin=dict(r=20, l=10, b=10, t=10))

    
    # if option_slctd == 1:
    #     for index1, item1 in enumerate(points_lx):

    #         fig1.add_trace(go.Scatter3d(x=item1,y=points_ly[index1],z=points_lz[index1], mode='markers',marker=dict(color="white", opacity=0.5)))



    return fig1, fig1

#fig1.show()

# #------------------------------------------------------------------------

#     #--------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
"""
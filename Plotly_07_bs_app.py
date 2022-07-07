import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly
from plotly import graph_objs as go
import json
import numpy as np
import pandas as pd


# ----------------------------------------------------------------
# App with dash_bootstrap_components

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX],
                    meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale=1.0'}]
                    )
app.title= "Mission Control"
# ------------------------------------------------------------------


# App Layout with dash_bootstrap_components

# ----------------
# TAB SPECKLE
#-----------------
graph_card= dbc.Card(dbc.CardBody([html.H6("STUDY CASES"),
                # dcc.Dropdown(id= "slct_data",
                # options=[
                #     {"label":"Level Organization","value":0},
                #     {"label":"Inclinations", "value":1},
                #     {"label":"Internal Angles", "value":2},
                #     {"label": "Neighbouring Angles", "value":3}],
                #     multi=False,
                #     value=0,
                #     style={'width':"70%"}
                #     ),
                    html.Iframe(src="https://speckle.xyz/embed?stream=15f8c49bb1&commit=e09a0b81fd&transparent=true", height= 600, width=600 )
                ]))

graph_card_2= dbc.Card(dbc.CardBody([html.H6("STORY BOARD"),
                                    html.Iframe(src="https://miro.com/app/embed/uXjVOZqFwoM=/?pres=1&frameId=3458764518626547972&embedId=15468631347", 
                                    height= 640 , width= 390)]))



# table_card_3=dbc.Card(dbc.CardBody([html.H6("Panel Information"),
#                                   dash_table.DataTable(id='table',
#                                 columns=[],
#                                 data=[],
#                                 style_cell={'padding': '2px'},
#                                 style_header={
#                                         'backgroundColor': 'white',
#                                         'border': '1px solid black',
#                                         'fontWeight': 'bold',
#                                         'textAlign':'left',
#                                         'font_size':'12px',
#                                         'font_case':'lower'
#                                         }
    
#                                     )
#                                     ]),style={'height':'30%'})

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


tab0_content= dbc.Row([html.H5("MAPPING CHANGING ECOSYSTEMS",className='mt-3 display-9 text-uppercase align-right text-secondary bg-secondary text-center'),
        dbc.Col([graph_card],width={'size':7, 'order':1},className='d-*-block '),
        dbc.Col([
            graph_card_2
            ],width={'size':5, 'order':2},align='top',md=5 )
        ],justify='center',className='d-*-block bg-light')
    

tab1_content= dbc.Row([
        dbc.Col([graph_card_1_t1],className='d-*-block bg-secondary shadow-sm'),
        dbc.Col([PDFtabs],className='d-*-block bg-secondary shadow-sm')
        ],justify='center',style={'height':'600'})

tab2_content=dbc.Row([
        dbc.Col(html.ObjectEl(data="assets\\210709_21061966_Quantity_list_Only_Demo.pdf",height=450, width=700),style={'height':'450','width':'10'})],
        justify='center',style={'height':'600'})


tabs= dbc.Tabs(
    [
        dbc.Tab(tab0_content)

        # dbc.Tab(tab1_content , label= 'BIM'),
        # dbc.Tab(label= 'Statics'),
        # dbc.Tab( tab2_content, label= 'Costs')

    ])


# ----------------------------------------------------------------

app.layout= dbc.Container([
    
    dbc.Row([
        dbc.Col(html.Div([html.Img(src="assets\\schueco_logo.PNG", height=20 , style={'float':'left' , 'display':'flex','position':'absolute','top':'35%','left':'1.5%'}),html.H1("LAB.PRO.FAB", 
        className='text-center bg-light text-dark mt-4 display-6 font-weight-bolder', style={'align': 'center', 'border-style':'none' })]
        ,style={'align-content': 'center', 'position':'relative', 'border-bottom':'double'}),
        width=10)],justify='center'), 
        dbc.Row([
        dbc.Col(dbc.CardHeader([tabs]), width={'size':10},xl=10)
    ],justify='center')

    ])
 
# ----------------------------------------------------------------
# CALLBACKS
# # Connect the plotly graphs with Dash Components 

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

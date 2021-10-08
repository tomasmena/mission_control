import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
from plotly import graph_objs as go
import dash_vtk
dash_vtk.Mesh()

# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)


#------------------------------------------------------------------------------
app=dash.Dash(__name__)
# Import data 
df=pd.read_csv("C:\\Dropbox\\00_TOMAS\\00_PC\\00_Projects\\Plotlling\\Analysis.csv")

# df=pd.read_csv("C:\\Dropbox\\00_TOMAS\\00_PC\\00_Projects\\Plotlling\\intro_bees.csv")
df= df.groupby(['Level_Panel#', 'I' , 'a' , 'b' , 'c','d','e','f' ]).mean()

df.reset_index(inplace=True)

print(df[:20])

# ------------------------------------------------------------------------------------

# App Layout

# app.layout=html.Div([

#     html.H1 ("Web Application Dashboards with Dash", style={'text-align':'center'}),

#     dcc.Dropdown(id="slct_year",
#                 options=[
#                     {"label":"2015","value":2015},
#                     {"label":"2016", "value":2016},
#                     {"label":"2017", "value":2017},
#                     {"label": "2018", "value":2018}],
#                     multi=False,
#                     value=2015,
#                     style={'width':"40%"}
#                     ),
        
#     html.Div(id='output_container',children=[]),
#     html.Br(),


#     dcc.Graph(id='my_bee_map',figure={})
# ])

# #------------------------------------------------------------------------

# # Connect the plotly graphs with Dash Components 

# @app.callback(
#     [Output(component_id='output_container',component_property='children'),
#      Output(component_id='my_bee_map', component_property='figure')],
#     [Input(component_id='slct_year', component_property='value')]
# )

# def update_graph(option_slctd):
#     print (option_slctd)
#     print (type(option_slctd))

#     container="The year chosen by the user was __ {}".format(option_slctd)

#     dff= df.copy()
#     dff= dff[dff["Year"] == option_slctd ]
#     dff=dff[dff["Affected by"] == "Varroa_mites"]

#     # fig= px.bar(
#     #     data_frame=dff,
#     #     x='State',
#     #     y='Pct of Colonies Impacted',
#     #     hover_data=['State','Pct of Colonies Impacted'],
#     #     labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
#     #     template='plotly_dark'
#     # )
#     fig= px.choropleth(

#         data_frame=dff,
#         locationmode= 'USA-states',
#         locations= 'state_code',
#         scope= "usa",
#         color='Pct of Colonies Impacted',
#         hover_data= ['State','Pct of Colonies Impacted'],
#         color_continuous_scale=px.colors.sequential.YlOrRd,
#         labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
#         template='plotly_dark'
#     )
#     return container,fig

#     #--------------------------------------------

# if __name__ == '__main__':
#     app.run_server(debug=True)
    
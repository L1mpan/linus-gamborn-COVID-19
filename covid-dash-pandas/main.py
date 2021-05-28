import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


    #Pandas
dfCases = pd.read_csv("Regional_Daily_Cases.csv")       #läser in csv filen till DataFramen 'dfCases'
dfDeaths = pd.read_csv("National_Daily_Deaths.csv")     #läser in csv filen till DataFramen 'dfDeaths'


    #Definera App
app = dash.Dash(                                        #definerar app så att man senare kan starta hemsidan
    external_stylesheets=[dbc.themes.BOOTSTRAP],        #importerar bootstrap
    meta_tags=[                                         #meta tags så att hemsidan ska vara responsiv till alla enheter
        {
            "name": "viewport", 
            "content": "width=device-width, initial-scale=1"
        }
    ],
)


    #Grafer
#1, linje graf, ritar ut med dagliga fall som y och datumet som x.
fig = px.line(dfCases, x="Date", y="Sweden_Total_Daily_Cases", labels={
    "Date": "Datum",
    "Sweden_Total_Daily_Cases": "Dagliga fall"
    }).update_layout({                                  #ändrar bakgrundsfärgen och självaste färgen på grafen 
        "plot_bgcolor": "#111111", 
        "paper_bgcolor": "#2C2F33",
    })
#2, histogram, ritar ut med medelvärdet av fall som y och datumet som x.
fig2 = px.histogram(dfCases, x="Date", y="Sweden_Total_Daily_Cases", histfunc='avg', labels={
    "Date": "Månad",
    "Sweden_Total_Daily_Cases": "Dagliga fall"
    }).update_layout({   
        "plot_bgcolor": "#111111", 
        "paper_bgcolor": "#2C2F33",
        })
#3, stapeldiagram, ritar ut med dagliga dödsfall som y och datumet som x.
fig3 = px.bar(dfDeaths, x="Date", y="National_Daily_Deaths", labels={
    "Date": "Dagar",
    "National_Daily_Deaths": "Dagliga dödsfall"
    }).update_layout({
        "plot_bgcolor": "#111111", 
        "paper_bgcolor": "#2C2F33",
    })


    #Header
sidebar_header = html.Div(                                                          #skapar en div som kallas för 'sidebar_header'
    [
        html.H1('Covid-19 Statistics'),                                             #skapar en H1 där det står en rubrik
        html.Div(
            [
                dbc.Nav(                                                            #skapar ett ul element med hjälp av dbc och lägger 4st li i den
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("Graph 1", href="/graph-1", active="exact"),
                        dbc.NavLink("Graph 2", href="/graph-2", active="exact"),
                        dbc.NavLink("Graph 3", href="/graph-3", active="exact"),
                    ],
                        horizontal=True,                                            #bestämmer att den ska vara display: horizontal
                        pills=True,                                                 #lägger på lite padding så att knapparna ser bättre ut
                        justified=True,
                ),
            ]
        )
    ],  
    #style atributes för 'sidebar_header' diven
    style={ "text-align": "center", 
            "background-color": "#2C2F33", 
            "color": "#FFFFFF",
    }
)

    #div som kallas för 'content', allt här i går att byta med hjälp av navbaren vilket länkar till en ny path
content = html.Div(id="page-content")

    #app.layout tar allt som vi har skrivit med hjälp av alla components och compilar allt in i hemsidans layout
app.layout = html.Div([dcc.Location(id="url"), sidebar_header, content])


    #callback, funktioner med if statements kollar pathname och beroende på pathname så byter den ut det som är innuti 'content' diven
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return  html.Div(
                    [
                        html.H1("Här är några grafer som visar data från Covid-19 pandemin")
                    ], 
                        style={                                 #ändrar style atributes för allt som går ändra i 'content' diven
                            "text-align": "center", 
                            "background-color": "#2C2F33", 
                            "color": "#FFFFFF",
                            "padding-top": "20px",
                            "padding-bottom": "100%",
                        }
                )
    elif pathname == "/graph-1":                                #elif som kollar ifall pathname stämmer med rätt path, och om den gör det så retunerar den diven in i 'content'
        return  html.Div(
                    [
                        html.H2('Dagliga Fall:'),               #rubrik för grafen
                        dcc.Graph(                              #dcc.Graph som har figure= vad figuren var definerad att heta. Alla grafer måste ha ett unikt id.
                            id='line-graph',
                            figure=fig
                        ),
                    ], 
                        style={
                            "text-align": "center", 
                            "background-color": "#2C2F33", 
                            "color": "#FFFFFF",
                            "padding-top": "20px",
                            "padding-bottom": "100%",
                        }
                )
    elif pathname == "/graph-2":                                        # ^ ^ ^
        return  html.Div(
                    [
                        html.H2('Avg Dagliga fall i varje månad:'),     # ^ ^ ^
                        dcc.Graph(                                      # ^ ^ ^
                            id='hist-graph',
                            figure=fig2
                        ),
                    ],  
                        style={"text-align": "center", 
                            "background-color": "#2C2F33", 
                            "color": "#FFFFFF",
                            "padding-top": "20px",
                            "padding-bottom": "100%",
                        }
                )
    elif pathname == "/graph-3":                                        # ^ ^ ^
        return  html.Div(
                    [
                        html.H2('Dödsfall:'),                           # ^ ^ ^
                        dcc.Graph(                                      # ^ ^ ^
                            id='bar-chart',
                            figure=fig3
                        ),
                    ], 
                        style={
                            "text-align": "center", 
                            "background-color": "#2C2F33", 
                            "color": "#FFFFFF",
                            "padding-top": "20px",
                            "padding-bottom": "100%",
                        }
                )
    # 404 meddelande ifall det är en path som inte finns
    return dbc.Jumbotron(                                           #om inget av elif ovan stämmer, retunerar den en bootstrap div till 'content' som ger Error: 404 Not found
        [
            html.Br(),
            html.H1("Error!", className="text-danger"),
            html.H1("404: Not found", className="text-danger"),
        ],
        style={                                                     #style atributes för bootstrap diven
            "background-color": "#2C2F33", 
            "color": "#FFFFFF",
            "padding-top": "20px",
            "padding-bottom": "100%",
        }
    )

    #startar hemsidan
if __name__ == "__main__":
    app.run_server(port=1111, debug=True)
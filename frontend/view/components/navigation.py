# Internal
from app import app
# External
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

header = dbc.Row(
    [
        dbc.Col(dbc.NavLink("PFinder", href="/", className="navbar-brand")),
        dbc.Col(
            [
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    id="navbar-toggle",
                ),
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    id="sidebar-toggle",
                ),
            ],
            width="auto",
            align="center",
        ),
    ]
)
links = dbc.Nav(
    [
        dbc.NavLink([html.I(['monetization_on'], className="material-icons"), 'Predict'],
                    href=f"/predict", id=f"page-predict-link"),
        dbc.NavLink([html.I(['apartment'], className="material-icons"), 'Property'],
                    href=f"/property", id=f"page-property-link"),
        dbc.NavLink([html.I(['public'], className="material-icons"), 'Map'],
                    href=f"/map", id=f"page-map-link")
    ],
    vertical=True,
    pills=True,
)
paths = [link.href for link in links.children]

component = html.Div(
    [
        header,
        html.Div(html.Hr(), id="blurb"),
        dbc.Collapse(links, id="collapse"),
    ],
    id='sidebar',
    className=''
)


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def switch_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def switch_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

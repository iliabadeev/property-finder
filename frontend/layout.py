# Internal
from view import View
from app import app, server
# External
import dash_html_components as html
from dash.dependencies import Output, Input


#######################################################################################
# LAYOUT
#######################################################################################
view = View(application=app)
app.layout = html.Div([view.url, view.navigation, view.content], id='layout')


# Page content controller
@app.callback(Output("page", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    return view[pathname]

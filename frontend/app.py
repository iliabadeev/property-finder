# External
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

#######################################################################################
# APP, SERVER
#######################################################################################
ICONS = {'href': 'https://fonts.googleapis.com/icon?family=Material+Icons',
         'rel': 'stylesheet'}

app = Dash(__name__,
           external_stylesheets=[BOOTSTRAP, ICONS],  # Bootstrap 4, icons
           meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
           prevent_initial_callbacks=True)  # For sidebar
server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Property Finder'

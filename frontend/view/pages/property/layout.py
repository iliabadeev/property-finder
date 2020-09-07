# Python
from __future__ import annotations
# Bound
from . import plots
# Internal
from app import app
from connection import BACKEND
# External
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

_IDs = BACKEND.request('GET', '/property/ids')
_IDs = sorted([id['id'] for id in _IDs])
_OPTIONS = [{'label': id, 'value': id} for id in _IDs]


@app.callback([Output(f'property__info', 'children'),
               Output(f'property__map', 'children')],
              [Input('property__button', 'n_clicks')],
              [State('property__selector', 'value')])
def get_property(n, property: 'int'):
    data = BACKEND.request('GET', f'/property/{property}')[0]
    information = [{'column': k, 'value': v} for k, v
                   in data.items()]
    table = plots.table(information=information)
    map = plots.map(latitude=data['latitude'], longitude=data['longitude'])
    return table, dcc.Graph(figure=map)

####################################################################################################
# View
####################################################################################################


selector = dcc.Dropdown(
    id=f'property__selector',
    className=f'property__selector',
    options=_OPTIONS,
    persistence=True
)
button = dbc.Button('Find', id=f'property__button', className=f'property__button',
                    outline=True, color='primary', size='lg')


info = dbc.Card([
    dbc.CardHeader(['Information'.title()]),
    dbc.CardBody([
        dcc.Loading(
            id=f'property__info__loading', type='circle',
            children=[dbc.Row([dbc.Col(id=f'property__info', md=12)])]
        )
    ], className='card_body--table')
])
map = dbc.Card([
    dbc.CardHeader(['Map'.title()]),
    dbc.CardBody([
        dcc.Loading(
            id=f'property__map__loading', type='circle',
            children=[dbc.Row([dbc.Col(id=f'property__map', md=12)])]
        )
    ])
])
content = dbc.Container(children=[])
content.children.append(dbc.Row([dbc.Col([selector], md=10),
                        dbc.Col([button], md=2)]))
content.children.append(info)
content.children.append(map)

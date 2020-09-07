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

_DATE_FORMAT_INPUT = 'YYYY-MM-DD'


@app.callback(
    [Output(f'avm_placeholder', 'children'),
     Output(f'transacted_placeholder', 'children')],
    [Input('predict__apply', 'n_clicks')],
    [State('predict__date_picker', 'start_date'),
     State('predict__date_picker', 'end_date'),
     State('predict__offer_type', 'value'),
     State('predict__bathrooms', 'value'),
     State('predict__bedrooms', 'value'),
     State('predict__cheques', 'value'),
     State('predict__sqft', 'value'),
     State('predict__location', 'value'),
     State('predict__latitude', 'value'),
     State('predict__longitude', 'value')])
def predict(n, valid_from: 'str', valid_to: 'str',
            offer_type: 'int', bedrooms: 'int', bathrooms: 'int',
            sqft: 'int', cheques: 'int', location_path: 'str',
            latitude: 'float', longitude: 'float'):
    params = {'valid_from': valid_from, 'valid_to': valid_to,
              'offer_type': offer_type, 'bedrooms': bedrooms,
              'bathrooms': bathrooms, 'sqft': sqft,
              'cheques': cheques, 'location_path': location_path,
              'latitude': latitude,   'longitude': longitude}
    avm = BACKEND.request('GET', '/model/avm/predict', params=params)['prediction']
    transacted = BACKEND.request('GET', '/model/transacted/predict', params=params)['probability']
    return plots.avm(prediction=avm), plots.transacted(prediction=transacted)




####################################################################################################
# View
####################################################################################################

content = dbc.Container(children=[])
form = [
    # Timing + Buttons
    dbc.Row([
        dbc.Col([
            html.Div('Valid:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.DatePickerRange(id='predict__date_picker', className='predict__selector',
                                start_date_placeholder_text='From...', end_date_placeholder_text='To...',
                                display_format=_DATE_FORMAT_INPUT, first_day_of_week=1,
                                persistence=True, persistence_type='session')
        ]),
        dbc.Col([
            dbc.Button('Clear', id='predict__clear', className='predict__button',
                       outline=True, color='danger', size='md'),
            dbc.Button('Predict', id='predict__apply', className='predict__button',
                       outline=True, color='primary', size='md')
        ], className='predict__buttons', md=4)
    ], className='predict__element'),
    #
    dbc.Row([
        dbc.Col([
            html.Div('Offer:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Dropdown(id='predict__offer_type', className='predict__selector',
                         options=[{'label': 1, 'value': 1}, {'label': 2, 'value': 2}],
                         persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Bathrooms:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__bathrooms', className='predict__input',
                      type='number', min=0, persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Bedrooms:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__bedrooms', className='predict__input',
                      type='number', min=0, persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Cheques:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__cheques', className='predict__input',
                      type='number', min=0, persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Sqaure Feets:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__sqft', className='predict__input',
                      type='number', min=1, persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Location:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__location', className='predict__input',
                      type='text', persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Latitude:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__latitude', className='predict__input',
                      type='number', min=-180, max=180,
                      persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
    dbc.Row([
        dbc.Col([
            html.Div('Longitude:', className='predict__label'),
        ], md=3),
        dbc.Col([
            dcc.Input(id='predict__longitude', className='predict__input',
                      type='number', min=-180, max=180,
                      persistence=True, persistence_type='session')
        ])
    ], className='predict__element'),
]

card = [
    dbc.Card([
        dbc.CardHeader(['Prediction'.title()]),
        dbc.CardBody([
            dcc.Loading(
                id=f'prediction_loading', type='circle',
                children=[
                    dbc.Row([dbc.Col(id='avm_placeholder', md=6),
                             dbc.Col(id='transacted_placeholder', md=6)], align='center'),
                ])
        ])

    ])

]
content.children.extend(form)
content.children.extend(card)

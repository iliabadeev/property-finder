# Python
from __future__ import annotations
#  Bound
from . import plots
# Internal
from connection import BACKEND
# External
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

content = list()
content.append(
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=plots.heatmap(pd.DataFrame(BACKEND.request('GET', '/map/price'))), id='map__price',
                          className='map__price')
            ])
        ])
    ], fluid=True, className='map')
)

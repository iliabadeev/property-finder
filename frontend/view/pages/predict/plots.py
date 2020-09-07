# Python
from __future__ import annotations
# External
import plotly.graph_objects as go
import dash_core_components as dcc


def avm(prediction: 'int'):
    indicator = go.Figure(go.Indicator(mode="number",
                                       title=dict(text='<i>PRICE</i>', font_size=25),
                                       value=prediction,
                                       number=dict(font_size=40, suffix=' AED')))
    return dcc.Graph(figure=indicator)


def transacted(prediction: 'float'):
    indicator = go.Figure(go.Indicator(mode="number",
                                       title=dict(text='<i>TRANSACTED</i>', font_size=25),
                                       value=prediction*100,
                                       number=dict(font_size=40, suffix=' %', valueformat='.1f')))
    return dcc.Graph(figure=indicator)

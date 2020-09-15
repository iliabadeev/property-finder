# Python
from __future__ import annotations
# Internal
# External
import dash_table as ddt
import plotly.graph_objs as go


def table(information: 'list'):
    columns = [{'name': 'column', 'id': 'column',
                'type': 'text', 'deletable': False, 'selectable': False},
               {'name': 'value', 'id': 'value',
                'type': 'text', 'deletable': False, 'selectable': False}]
    table = ddt.DataTable(
        id='property__info__table',
        columns=columns,
        data=information,
        page_action='native',
        page_size=20,
        row_selectable=False,
        cell_selectable=True,
        style_as_list_view=True,
        style_cell={'textAlign': 'center'},
        style_data_conditional=[{'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(245, 245, 245)'}],
        style_header={'backgroundColor': 'rgb(220, 220, 220)',
                      'fontWeight': 'bold'},
    )
    return table


def map(latitude: 'float', longitude: 'float'):
    figure = go.Figure()
    figure.add_trace(go.Scattermapbox(
        connectgaps=False,
        lat=[latitude],
        lon=[longitude],
        mode='markers',
        marker=dict(size=40)
    ))
    figure.update_layout(
        autosize=True,
        mapbox=dict(style='carto-darkmatter', zoom=11, bearing=0, pitch=30,
                    center={"lon": longitude, "lat": latitude})
    )
    figure.update_layout(
        font=dict(size=15, family='Roboto', color='#333'),
        height=600,
        margin=dict(l=0, r=0, b=0, t=0, pad=0)
    )
    return figure



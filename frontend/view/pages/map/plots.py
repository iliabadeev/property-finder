# Python
from __future__ import annotations
# External
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go


def heatmap(data: 'pd.DataFrame') -> 'go.Figure':
    figure = go.Figure()
    figure.add_trace(go.Densitymapbox(
        lat=data['LatArea'],
        lon=data['LonArea'],
        z=data['Price'],
        radius=30,
        showscale=False,
        showlegend=False,
        zmin=100,
        zmax=10000
    ))
    figure.update_layout(
        autosize=True,
        mapbox=dict(style='carto-darkmatter', zoom=5, bearing=0, pitch=30,
                    center={"lat": data['LatArea'].median(), "lon": data['LonArea'].median()})
    )
    figure.update_layout(
        font=dict(size=15, family='Roboto', color='#333'),
        margin=dict(l=0, r=0, b=0, t=0, pad=0)
    )
    return figure

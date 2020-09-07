# External
import dash_bootstrap_components as dbc
import dash_html_components as html

_BASE_VIEW = 'base'

index = \
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(id=f'{_BASE_VIEW}__logo'),
                html.P(f"Welcome!", id=f'{_BASE_VIEW}__brand')
            ], id=_BASE_VIEW)
        ])
    ], fluid=True)

p404 = \
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(id=f'{_BASE_VIEW}__logo'),
                html.P(f"404", id=f'{_BASE_VIEW}__brand')
            ], id=_BASE_VIEW)
        ])
    ], fluid=True)

p401 = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.A(html.Div(id=f'{_BASE_VIEW}__logo', className='login_link')),
                html.P("Property Finder", id=f'{_BASE_VIEW}__brand')
            ], id=_BASE_VIEW)
        ])
    ], fluid=True)

# Python
from __future__ import annotations
# Bound
from .components import url, content, navigation
from .pages import base, predict, property, map
# Typing
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dash import Dash

_PAGES = {
    '/map': map.content,
    '/property': property.content,
    '/predict': predict.content,
    '/': base.index,
    404: base.p404,
    401: base.p401
}


class View:

    def __init__(self, application: 'Dash'):
        self._app = application
        # Main
        self.url = url.component
        self.content = content.component
        self.navigation = navigation.component
        self.pages = _PAGES

    def __getitem__(self, item):
        return self.pages.get(item, self.pages[404])

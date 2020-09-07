# Python
from __future__ import annotations
# External
import requests
# Typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, Union, Dict, List, Tuple


class Connection:

    def __init__(self):
        self.host = 'http://0.0.0.0:5000/api/v1'
        self._session: 'Optional[requests.Session]' = None

    @property
    def session(self) -> 'requests.Session':
        # TODO: add better session control
        if not self._session:
            self._session = requests.Session()
        return self._session

    def request(self, method: str, endpoint: str, *, params: 'Union[Dict, bytes]' = None,
                data: 'Union[Dict, List[Tuple], bytes]' = None) -> 'requests.Response':
        # Prepare the final endpoint
        url = self.host + endpoint
        # Prepare parameters
        request = requests.Request(method=method, url=url, params=params, data=data).prepare()
        return self.session.send(request).json()

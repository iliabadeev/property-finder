# Python
from __future__ import annotations
from pathlib import Path
import sqlite3
# External
import pandas as pd
# Typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, Union, List
_LOCATION = Path(__file__).parent
_NAME = 'database.sqlite'


class DataBase:

    def __init__(self):
        pass

    @property
    def connection(self):
        return sqlite3.connect(_LOCATION / _NAME)
    
    def read(self, query: 'str', dataframe: 'bool' = False) -> 'Union[List, pd.DataFrame]':
        """
       Wrapper for SELECT clause. Can return pandas DataFrame if specified.
       """
        # Prepare cursor
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except Exception:
            self.connection.close()
        # Get results
        result = cursor.fetchall()
        # to DataFrame if required
        if dataframe:
            columns = [column[0] for column in cursor.description]
            result = pd.DataFrame(data=result, columns=columns)
        # Clean cursor
        cursor.close()
        # Return
        return result


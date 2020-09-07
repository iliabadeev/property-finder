# Python
from __future__ import annotations
import os
# External
import psycopg2 as driver
import pandas as pd
# Typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, Union, List
    from psycopg2.extensions import connection


class DataBase:
    """
    Object for database connection + sugar methods that helps interact with the DB
    """

    def __init__(self):
        self._connection: 'Optional[connection]' = None

    @property
    def connection(self) -> 'connection':
        """
        Open connection if closed or not initialized.
        """
        if not self._connection or self._connection.closed != 0:
            self._connection = driver.connect(
                host=os.environ['PG_SERVER'],
                port=os.environ['PG_PORT'],
                user=os.environ['PG_USER'],
                password=os.environ['PG_PASSWORD'],
                dbname=os.environ['PG_DATABASE']
            )
        return self._connection

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
            columns = [column.name for column in cursor.description]
            result = pd.DataFrame(data=result, columns=columns)
        # Clean cursor
        cursor.close()
        # Return
        return result


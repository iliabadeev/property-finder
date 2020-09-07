# Internal
from core.dbms import DATABASE


def all():
    query = 'SELECT * FROM poi'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')


def by_id(id: 'int'):
    query = f'SELECT * FROM poi WHERE id == {id}'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')


def ids():
    query = f'SELECT DISTINCT id FROM poi'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')


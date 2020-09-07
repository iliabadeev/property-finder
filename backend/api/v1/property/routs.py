# Internal
from core.dbms import DATABASE


def all():
    query = 'SELECT * FROM listings'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')


def by_id(id: 'int'):
    query = f'SELECT * FROM listings WHERE id == {id}'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')


def ids():
    query = f'SELECT DISTINCT id FROM listings'
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')

# Internal
from core.dbms import DATABASE


def price():
    query = """
    SELECT  round(latitude, 4) LatArea,
            round(longitude, 4) LonArea,
            round(avg(price/sqft), 2) Price
    FROM    listings
    GROUP   BY LatArea, LonArea
    ORDER   BY price DESC"""
    result = DATABASE.read(query, dataframe=True)
    return result.to_json(orient='records')
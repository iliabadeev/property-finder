# Python
from __future__ import annotations
from dataclasses import dataclass
# External
import pandas as pd

_OPTIMAL_TYPES = {
    'valid_from': 'datetime64[s]',
    'valid_to': 'datetime64[s]',
    'offer_type': 'uint8',
    'bedrooms': 'uint8',
    'bathrooms': 'uint8',
    'sqft': 'uint32',
    'cheques': 'uint8',
    'price': 'uint64',
    'transacted': 'uint8',
    'location_path': 'str',
    'latitude': 'float32',
    'longitude': 'float32'
}


@dataclass
class Property:
    valid_from: 'str' = ''
    valid_to: 'str' = ''
    offer_type: 'int' = 0
    bedrooms: 'int' = 0
    bathrooms: 'int' = 0
    sqft: 'int' = 0
    cheques: 'int' = 0
    price: 'int' = 0
    transacted: 'int' = 0
    location_path: 'str' = ''
    latitude: 'float' = 0.0
    longitude: 'float' = 0.0

    def from_dictionary(self, dictionary: 'dict') -> None:
        for attribute, value in dictionary.items():
            if getattr(self, attribute, None) is not None:
                setattr(self, attribute, value)

    @property
    def dataframe(self) -> 'pd.DataFrame':
        attributes = {k: [v] for k, v in self.__dict__.items()}
        frame = pd.DataFrame.from_dict(attributes)
        frame = frame.astype(_OPTIMAL_TYPES, errors='ignore')
        return frame

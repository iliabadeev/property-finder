# Python
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import json
# External
import pandas as pd
import h3.api.basic_int as H3
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
# Typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable

_LOCATION = Path(__file__).parent


######################################
# Wrappers
######################################
class PipelineWithNames(Pipeline):

    def get_feature_names(self):
        return self.steps[-1][1].get_feature_names()


class SimpleImputerWithNames(SimpleImputer):

    @staticmethod
    def get_feature_names():
        return ['imputed']


class UntouchedTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X: 'pd.DataFrame', y=None):
        return self

    @staticmethod
    def transform(X: 'pd.DataFrame', y=None):
        return X

    @staticmethod
    def get_feature_names():
        return ['untouched']


######################################
# Features
######################################
class TimingTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, start: 'str', end: 'str'):
        self.start = start
        self.end = end

    def fit(self, X: 'pd.DataFrame', y=None):
        return self

    def transform(self, X: 'pd.DataFrame', y=None):
        result = pd.DataFrame([])
        result['days'] = (X[self.end] - X[self.start]).dt.days
        result['quarter'] = X[self.start].dt.quarter
        result['month'] = X[self.start].dt.month
        return result

    @staticmethod
    def get_feature_names():
        return ['days', 'quarter', 'month']


class BathBedRatioTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, bathrooms: 'str', bedrooms: 'str'):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms

    def fit(self, X: 'pd.DataFrame', y=None):
        return self

    def transform(self, X: 'pd.DataFrame', y=None):
        return (X[self.bathrooms] / X[self.bedrooms]).to_frame(name='ratio')

    @staticmethod
    def get_feature_names():
        return ['ratio']


################################################################
# GeoData
###############################################################

_RESOLUTIONS = (6, 7, 8, 9)
_LATITUDE = 'latitude'
_LONGITUDE = 'longitude'


def _hexagon(resolution: 'int') -> 'Callable[[float, float, int], int]':
    return lambda column: H3.geo_to_h3(column[_LATITUDE], column[_LONGITUDE], resolution)


def _name(resolution: 'int') -> 'str':
    return f'hexagon_{resolution}'


class _ObjectNearBy:
    precomputed = _LOCATION / 'nearby.json'

    def __init__(self):
        self.objects = self.load()

    def precompute(self):
        # Load objects
        objects = pd.read_pickle(_LOCATION.parent / 'loading' / 'poi.pkl.gzip')
        # Placeholder for the output
        result = defaultdict(dict)
        # Per category, e.g. Metro
        for category in tuple(objects['category'].unique()):
            # Select only relevant
            relevant = objects.query('category == @category').copy()
            # Per resolution
            for resolution in _RESOLUTIONS:
                # Compute Hexagons from coordinates and store them to the result placeholder
                result[category.lower()][_name(resolution)] =\
                    relevant.apply(_hexagon(resolution), axis=1).value_counts().to_dict()
        # Save in json
        with self.precomputed.open('w') as dump:
            json.dump(dict(result), dump)

    def load(self):
        try:
            # Try to open if exists
            with self.precomputed.open('rb') as precomputed:
                objects = json.load(precomputed)
        except Exception as e:
            # Recompute (dump again)
            self.precompute()
            # Open
            objects = self.load()
        return objects

    def __getitem__(self, item):
        return self.objects.get(item)


_NEARBY = _ObjectNearBy()


class H3AreasTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X: 'pd.DataFrame', y=None):
        return self

    @staticmethod
    def transform(X: 'pd.DataFrame', y=None):
        result = pd.DataFrame([])
        for resolution in _RESOLUTIONS:
            result[_name(resolution)] = X.apply(_hexagon(resolution), axis=1)
        return result

    @staticmethod
    def get_feature_names():
        return [_name(resolution) for resolution in _RESOLUTIONS]


class H3PricePerAreaTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, price: 'str', sqft: 'str'):
        self.price = price
        self.sqft = sqft
        # Private
        self._ppa = dict()

    def fit(self, X: 'pd.DataFrame', y=None):
        price_per_ft = (X[self.price] // X[self.sqft].replace(0, 1)).rename('price_per_ft')
        self._ppa['global'] = price_per_ft.mean().round()
        for resolution in _RESOLUTIONS:
            # Compute absolute price per area (per property)
            ppa = X.apply(_hexagon(resolution), axis=1).to_frame(name=_name(resolution)).join(price_per_ft)
            # Find mean per area
            ppa = ppa.groupby(_name(resolution)).mean()['price_per_ft'].round()
            # Save as fitted parameter
            self._ppa[_name(resolution)] = ppa.to_dict()
        return self

    def transform(self, X: 'pd.DataFrame', y=None):
        results = pd.DataFrame([])
        for resolution in _RESOLUTIONS:
            results[f'{_name(resolution)}_ppa'] = X.apply(_hexagon(resolution), axis=1)\
                .map(lambda x: self._ppa[_name(resolution)].get(x, self._ppa['global']))
        return results

    @staticmethod
    def get_feature_names():
        return [f'{_name(resolution)}_ppa' for resolution in _RESOLUTIONS]


class H3NearbyTransformer(BaseEstimator, TransformerMixin):

    def fit(self, X: 'pd.DataFrame', y=None):
        return self

    @staticmethod
    def transform(X: 'pd.DataFrame', y=None):
        results = pd.DataFrame([])
        for resolution in _RESOLUTIONS:
            area = X.apply(_hexagon(resolution), axis=1)
            for category in _NEARBY.objects.keys():
                results[f'{category}_{_name(resolution)}'] = area.map(
                    lambda x: _NEARBY[category][_name(resolution)].get(str(x), 0)
                )
        return results

    @staticmethod
    def get_feature_names():
        return [f'{category}_{_name(resolution)}'
                for resolution in _RESOLUTIONS
                for category in _NEARBY.objects.keys()]

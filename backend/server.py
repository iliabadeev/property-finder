# Python
from __future__ import annotations
import os
# Internal
import api
# External
from flask import Flask
from flask import jsonify
# Typing

# Create serving instance
server = Flask(__name__)


# Index -> server health indicator
@server.route('/', methods=['GET'])
def health():
    response = {
        'alive': 'ok',
        'environment': dict(os.environ.items())
    }
    return jsonify(response)


###########
# API
###########
# Properties
server.add_url_rule('/api/v1/property/all', endpoint='api.v1.property.routs.all',
                    view_func=api.v1.property.routs.all, methods=['GET', 'POST'])
server.add_url_rule('/api/v1/property/ids', endpoint='api.v1.property.routs.ids',
                    view_func=api.v1.property.routs.ids, methods=['GET', 'POST'])
server.add_url_rule('/api/v1/property/<int:id>', endpoint='api.v1.property.routs.by_id',
                    view_func=api.v1.property.routs.by_id, methods=['GET'])
# Locations
server.add_url_rule('/api/v1/location/all', endpoint='api.v1.location.routs.all',
                    view_func=api.v1.location.routs.all, methods=['GET', 'POST'])
server.add_url_rule('/api/v1/location/ids', endpoint='api.v1.location.routs.ids',
                    view_func=api.v1.location.routs.ids, methods=['GET', 'POST'])
server.add_url_rule('/api/v1/location/<int:id>', endpoint='api.v1.location.routs.by_id',
                    view_func=api.v1.location.routs.by_id, methods=['GET'])
# Models
server.add_url_rule('/api/v1/model/avm/predict', endpoint='api.v1.model.avm.routs.predict',
                    view_func=api.v1.model.avm.routs.predict, methods=['GET', 'POST'])
server.add_url_rule('/api/v1/model/transacted/predict', endpoint='api.v1.model.transacted.routs.predict',
                    view_func=api.v1.model.transacted.routs.predict, methods=['GET', 'POST'])

# Maps
server.add_url_rule('/api/v1/map/price', endpoint='api.v1.map.price.routs',
                    view_func=api.v1.map.routs.price, methods=['GET'])

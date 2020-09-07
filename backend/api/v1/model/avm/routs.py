# Internal
from core.structures import Property
from core.preprocessing import PIPELINE
from core.evaluation import MODEL_AVM
# External
import pandas as pd
from flask import request, jsonify


def predict():
    property = Property()
    property.from_dictionary(request.args)
    features = pd.DataFrame(PIPELINE.transform(property.dataframe), columns=PIPELINE.get_feature_names())
    return jsonify({'prediction': int(MODEL_AVM.predict(features)[0])})

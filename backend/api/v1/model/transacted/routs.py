# Internal
from core.structures import Property
from core.preprocessing import PIPELINE
from core.evaluation import MODEL_TRANSACTED
# External
import pandas as pd
from flask import request, jsonify


def predict():
    property = Property()
    property.from_dictionary(request.args)
    features = pd.DataFrame(PIPELINE.transform(property.dataframe), columns=PIPELINE.get_feature_names())
    return jsonify({'prediction': float(MODEL_TRANSACTED.predict(features)[0]),
                    'probability': float(MODEL_TRANSACTED.predict_proba(features)[0][1])})

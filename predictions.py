import pickle
import numpy as np
import pandas as pd
import joblib
from flask import request, jsonify
from flask_restplus import Resource
from restplus import api
from parsers import clinical_fields
import joblib
from features import FEATURES

MODEL = joblib.load('model_xgb_11features.pkl')


namespace = api.namespace('covid_prediction', description='Predição baseada em dados de hemograma')

#@namespace.route('/check')
#class check(Resource):
#	def get(self):
#		return '1.0.1'




@namespace.route('/predict')
class Predict(Resource):

    @api.expect(clinical_fields)
    def post(self):

        args = clinical_fields.parse_args(request)
        x_list, missing_data = parse_argmts(args)

        x_array = np.array([x_list])

        prediction = MODEL.predict(x_array)
        predict_proba = MODEL.predict_proba(x_array)

        if prediction == 0:
            PREDICTED = 'Negative'
            PREDICT_PROBABILITY = round(predict_proba[0][0], 3)

        else:
            PREDICTED = 'Positive'
            PREDICT_PROBABILITY = round(predict_proba[0][1], 3)

        response = dict(PREDICTED=PREDICTED, CONFIDENCE= str(PREDICT_PROBABILITY))
        return jsonify(response)
        
        

	
def parse_argmts(request_dict):
	"""parse model features from incoming requests formatted in JSON"""
	missing_data = False
	request_dict = dict(request_dict)
	x_list = []
	for feature in FEATURES:
		value = request_dict.get(feature, None)
		if value:
			x_list.append(value)
		else:
			x_list.append(0)
			missing_data= True
			
	return x_list, missing_data



        

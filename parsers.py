from flask_restplus import reqparse



clinical_fields = reqparse.RequestParser()
# required


clinical_fields.add_argument('basophils_count', type=float, required=True, help='uL')
clinical_fields.add_argument('eosinophils_count', type=float, required=True, help='uL')
clinical_fields.add_argument('lymfocytes_count', type=float, required=True, help='uL')
clinical_fields.add_argument('monocytes_count', type=float, required=True, help='uL')
clinical_fields.add_argument('neutrophils_count', type=float, required=True, help='uL')
clinical_fields.add_argument('hemoglobin', type=float, required=True, help='g/dL')
clinical_fields.add_argument('mch', type=float, required=True, help='pg')
clinical_fields.add_argument('mchc', type=float, required=True, help='pg')
clinical_fields.add_argument('platelets_count', type=float, required=True, help='uL')
clinical_fields.add_argument('age', type=float, required=True, help='years')
clinical_fields.add_argument('gender', type=float, required=True, help='0:Male, 1:Female')




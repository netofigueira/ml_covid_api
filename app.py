from restplus import api
from predictions import namespace as prediction_namespace
from flask import Flask, Blueprint, redirect

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')

api.init_app(blueprint)
api.add_namespace(prediction_namespace)
app.register_blueprint(blueprint)

@app.route('/', methods=['GET'])
def main():
    return redirect('/api')


@app.route('/check', methods=['GET'])
def check():
    return '1.0.1'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    
    


# Import your dependencies
from flask import Flask, jsonify, request
from models import setup_db, Plant
from flask_cors import CORS, cross_origin
# Define the create_app function
def create_app(test_config=None):
    # Create and configure the app
    # Include the first parameter: Here, __name__is the name of the current Python module.
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
        return response

    @app.route('/')
    # simple decorator that allows cross origin on a specific end point
    # @cross_origin
    def hello_world():
        return jsonify({'message':'Hello, World!'})
    # Return the app instance
    return app
from flask import Flask
from flask_cors import CORS
from app import create_app

app = create_app()

CORS(app)

@app.route('/')
def index():
    return 'Welcome to Pesa App'

if __name__ == '__main__':
    app.run(debug=True)

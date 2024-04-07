from flask import Flask
from markupsafe import escape

print({__name__})
app = Flask(__name__)

@app.route('/')
def index():
    return 'The server is running!'

@app.route('/<name>')
def greet(name):
    return f'Hello, {escape(name)}!'
## add python venv environment with: python -m venv venv / vevn\Scripts\activate
## add flask to requirements.txt with: flask==1.1.2
## from flask import Flask
## app = Flask(__name__)
## @app.route('/') -> it's binds the function to the URL
## @app.route('/<parameter>')
## a route returns a html format by default, but it can be changed with the return statement
## f'{parameter}'
## escape(parameter) from markupsafe package
## @app.route('/<int:id>') -> <[ int | string | float | path | uuid ]:parameter_keywork>
## It's a good practice to a trailing slash in the URL like: /greet/ instead of /greet
## 
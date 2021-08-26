from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Hello World!'
        return render_template('index.html', page_title=title)

    return app
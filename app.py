from flask import Flask
from flask_bootstrap import Bootstrap
from controller import controller

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(controller)

if __name__ == '__main__':
    app.run()

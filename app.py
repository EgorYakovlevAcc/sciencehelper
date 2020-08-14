from flask import Flask
from flask_bootstrap import Bootstrap
from controller import main_router

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(main_router)

if __name__ == '__main__':
    app.run()

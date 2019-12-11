from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_bcrypt import Bcrypt
from flask_restful import Api

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ohya.db'
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
api = Api(app)

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app():
    # app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from classstock.routes import classstock
    from stock.routes import stock
    from manage.routes import ohyamanage
    from main.routes import main
    app.register_blueprint(classstock)
    app.register_blueprint(stock)
    app.register_blueprint(ohyamanage)
    app.register_blueprint(main)

    return app

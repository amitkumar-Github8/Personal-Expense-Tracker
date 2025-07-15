from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import *
from models.db import mysql
from routes.auth import auth_bp
from routes.expenses import expense_bp

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
jwt = JWTManager(app)
mysql.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(expense_bp, url_prefix='/api/expenses')

if __name__ == '__main__':
    app.run(debug=True)

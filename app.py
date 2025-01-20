from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from views.auth import auth_bp
from views.user import user_bp
from views.item import item_bp

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)

if __name__ == "__main__":
    app.run(debug=True)
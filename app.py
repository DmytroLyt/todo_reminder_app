from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)

with app.app_context():
    db.create_all()

from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(task_bp, url_prefix="/tasks")

if __name__ == "__main__":
    app.run()

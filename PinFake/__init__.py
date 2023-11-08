from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)  #criar app flask com o nome da pasta atual
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgresql://banco_pinfake_user:1W0EMERyk0EEoXwVUvighK9UYOgZUUSO@dpg-cl5orkk72pts73eqem80-a/banco_pinfake")
app.config["SECRET_KEY"] = "2720af2a2150f857eabd221fb77575c135eb953f"
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fotos_posts")

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from PinFake import routes
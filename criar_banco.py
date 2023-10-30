from PinFake import database, app
from PinFake.models import Usuario, Foto       #importar as classes da models

with app.app_context():
    database.create_all()
#criará a estrutura do banco de dados
from PinFake import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader      #diz para o login manager que essa função que carrega um usuario
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):      #Cria o obj "Usuario" no BD
    id = database.Column(database.Integer, primary_key=True)       # dentro da classe ficam as colunas do BD ou relações       
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    def is_active(self):
        return True


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao =database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
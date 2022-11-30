from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object('config')

CORS(app)

jwt = JWTManager(app)
db  = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

server = Server(host="0.0.0.0", port=os.getenv('PORT', 5000))
manager.add_command("runserver", server)
manager.add_command('db', MigrateCommand)

import Messages
from translation import error_messages
from app.components import fieldsFormatter

from app.models.usuarioTable import Usuario
from app.models.controllerTable import Controller
from app.models.regraTable import Regra
from app.models.cargoTable import Cargo
from app.models.perfilTable import Perfil

from app.models.cidadeTable import Cidade
from app.models.estadoTable import Estado
from app.models.paisTable import Pais

from app.models.pratoTable import Prato
from app.models.alunoTable import Aluno
from app.models.cardapioTable import Cardapio
from app.models.tipoRefeicaoTable import TipoRefeicao
from app.models.refeicaoTable import Refeicao
from app.models.alunoRefeicaoTable import AlunoRefeicao
from app.models.avaliacaoTable import Avaliacao

from app.model_schema.usuarioSchema import UsuarioAddSchema, UsuarioEditSchema
from app.model_schema.perfilSchema import PerfilAddSchema
from app.model_schema.authSchema import AuthLoginSchema
from app.model_schema.cadastroSchema import CadastroAddSchema
from app.model_schema.pratoSchema import PratoAddSchema
from app.model_schema.cardapioSchema import CardapioAddSchema
from app.model_schema.tipoRefeicaoSchema import TipoRefeicaoAddSchema
from app.model_schema.refeicaoSchema import RefeicaoAddSchema

from app.controllers import usuarioController
from app.controllers import authController
from app.controllers import perfilController
from app.controllers import cargoController
from app.controllers import cidadeController
from app.controllers import pratoController
from app.controllers import cardapioController
from app.controllers import tipoRefeicaoController
from app.controllers import refeicaoController


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Registrar el Blueprint - Corregido el import
from app.routes import bp
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
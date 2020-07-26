from flask import Flask
from flask_sqlalchemy import SQLALchemy
from app import config

app = Flask(__name__)    
app.config.from_object(config) # carga variables de configuración
db = SQLALchemy(app) # objeto que representa la BD

# rutas
@app.route('/')
def inicio():
    return 'Hello, World!' # esto habría que cambiarlo por: un render_template("inicio.html")

# errores
@app.errorhandler(404)
def page_not_found(error):
    return 'Error 404' # esto habría que cambiarlo por: render_template("error.html", error="Página no encontrada"), 404


if __name__ == '__main__':
       app.run()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    idpediddo = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    tamanio = db.Column(db.String(20), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    champi = db.Column(db.Boolean, default=False)
    jamon = db.Column(db.Boolean, default=False)
    pina = db.Column(db.Boolean, default=False)
    subtotal = db.Column(db.Float, nullable=False)

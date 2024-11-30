from app import db

class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float)
    fecha = db.Column(db.Date)
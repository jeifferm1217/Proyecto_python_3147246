from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Productos(BASE):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    nombre_producto = Column(String(100))
    descripcion = Column(String(500))
    imagen = Column(String(255))
    precio = Column(DECIMAL(10, 2))
    stock = Column(Integer)
    tipo = Column(Integer)
    fecha_creacion = Column(DateTime)

from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Albumes(BASE):
    __tablename__ = "albumes"
    id_album = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    titulo = Column(String(100))
    descripcion = Column(String(500))
    portada = Column(String(255))
    fecha_lanzamiento = Column(Date)
    precio = Column(DECIMAL(10, 2))
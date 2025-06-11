from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Publicaciones(BASE):
    __tablename__ = "publicaciones"
    id_publicacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    titulo = Column(String(50))
    contenido = Column(String(500))
    imagen = Column(String(255))
    media = Column(String(50))
    fecha_publicacion = Column(DateTime)
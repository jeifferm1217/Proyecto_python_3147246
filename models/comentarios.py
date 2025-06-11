from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Comentarios(BASE):
    __tablename__ = "comentarios"
    id_comentario = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"))
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    comentario = Column(String(500))
    fecha_comentario = Column(DateTime)
from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Reacciones(BASE):
    __tablename__ = "reacciones"
    id_reaccion = Column(Integer, primary_key=True)
    tipo_reaccion = Column(String(20))
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"))
    fecha_reaccion = Column(DateTime)

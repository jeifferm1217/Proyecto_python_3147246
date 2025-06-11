from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Seguidores(BASE):
    __tablename__ = "seguidores"
    id_seguidor = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_seguido = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_seguimiento = Column(DateTime)
from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Comunidades (BASE):
    __tablename__ = "comunidades"
    id_comunidad = Column(Integer,primary_key=True)
    id_usuario = Column(Integer,ForeignKey ("usuarios.id_usuario"))
    descripcion = Column(String(100))
    rangos = Column(Integer)
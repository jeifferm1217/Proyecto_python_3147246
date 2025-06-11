from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Reproducciones(BASE):
    __tablename__ = "reproducciones"
    id_reproduccion = Column(Integer, primary_key=True)
    id_cancion = Column(Integer,ForeignKey("canciones.id_cancion"))
    id_usuario = Column(Integer,ForeignKey("usuarios.id_usuario"))
    fecha_reproduccion = Column(DateTime)
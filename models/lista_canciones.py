from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Lista_Canciones(BASE):
    __tablename__ = "lista_canciones"
    id_lista = Column(Integer, primary_key=True)
    id_cancion = Column(Integer, primary_key=True)

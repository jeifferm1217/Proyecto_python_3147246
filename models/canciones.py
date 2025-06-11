from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Canciones(BASE):
    __tablename__= "canciones"
    id_cancion = Column(Integer,
                primary_key=True
                )    
    id_usuario = Column(Integer,ForeignKey("usuarios.id_usuario"))
    Titulo = Column(String(50))
    Descripcion = Column(String(50))
    id_genero = Column(Integer,ForeignKey("genero.id_genero"))
    id_album= Column(Integer,ForeignKey("albumes.id_album"))
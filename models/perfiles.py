from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Perfiles(BASE):
    __tablename__="perfiles"
    id_perfil = Column(Integer, 
                primary_key=True)
    id_usuario = Column(Integer,ForeignKey("usuarios.id_usuario") )
    nombre_artista =Column(String(50))
    biografia = Column (String(100))
    foto_perfil = Column(String(100))
    genero_musical = Column(String(50))
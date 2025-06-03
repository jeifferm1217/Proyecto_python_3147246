from .database import BASE
from sqlalchemy import Column, Integer, String, ForeignKey

#crear la base de modelo(entidad)
class Usuarios(BASE):
    __tablename__= "usuarios"
    id_usuario= Column(Integer,
                primary_key=True
                )
    nombre_usuario = Column(String(50))
    email = Column(String(100))
    contraseña = Column(String(50))
    telefono = Column (String(30))
class Perfiles(BASE):
    __tablename__="perfiles"
    id_perfil = Column(Integer, 
                primary_key=True)
    id_usuario = Column(Integer,ForeignKey("usuarios.id_usuario") )
    nombre_artista =Column(String(50))
    biografia = Column (String(100))
    foto_perfil = Column(String(100))
    genero_musical = Column(String(50))

class Canciones(BASE):
    __tablename__= "canciones"
    id_canciones = Column(Integer,
                primary_key=True
                )    
    id_usuario = Column(Integer,
                        ForeignKey("usuarios.id_usuario")
                         )
    Titulo = Column(String(50))
    Descripcion = Column(String(50))
    Portada = Column(String(50))
    id_genero = Column(Integer,
                       ForeignKey("genero.id_genero")
                       )
class Genero(BASE):
    __tablename__= "genero"
    id_genero = Column(Integer,
                primary_key=True
                )    
    genero = Column(String(50)) 
    
                            
        

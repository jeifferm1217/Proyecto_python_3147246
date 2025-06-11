from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class permisos_reproduccion(BASE):
    __tablename__= "permisos_reproduccion"
    id_permiso = Column(Integer, primary_key=True)
    id_cancion = Column(Integer, ForeignKey("canciones.id_cancion"))
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    permiso = Column(String(50))
    activo = Column(Boolean)
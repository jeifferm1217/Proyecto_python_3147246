from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Misiones_Comunidades(BASE):
    __tablename__ = "misiones_comunidades"
    id_mision = Column(Integer, primary_key=True)
    id_comunidad =Column(Integer,ForeignKey("comunidades.id_comunidad"))
    id_usuario = Column(Integer,ForeignKey ("usuarios.id_usuario"))
    titulo = Column(String(100))
    descripcion = Column(String(500))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    recompensa_puntos = Column(Integer)
    estado = Column(Integer)
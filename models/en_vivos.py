from db import BASE

from sqlalchemy import Enum,Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean
from models.enums import Estado_Envivo

class En_Vivos(BASE):
    __tablename__ = "en_vivos"
    id_envivo = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    titulo = Column(String(100))
    descripcion = Column(String(500))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    url_stream = Column(String(255))
    estado = Column(Enum(Estado_Envivo))
from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Derechos_Autor(BASE):
    __tablename__ = "derechos_autor"
    id_registro = Column(Integer, primary_key=True)
    id_cancion = Column(Integer)
    nombre_autor = Column(String(40))
    porcentaje_royalties = Column(DECIMAL(5, 2))
    fecha_acuerdo = Column(Date)
    documento_legal = Column(String(1000))
    activo = Column(Boolean)
    id_usuario_autor = Column(Integer, ForeignKey("usuarios.id_usuario"))
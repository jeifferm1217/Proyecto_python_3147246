from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Listas_Reproducciones(BASE):
    __tablename__ = "lista_reproducciones"
    id_lista = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    nombre_lista = Column(String(100))
    descripcion = Column(String(500))
    privada = Column(Boolean)
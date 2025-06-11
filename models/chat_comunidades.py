from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Chat_Comunidad(BASE):
    __tablename__ = "chat_comunidad"
    id_chat_comunidad = Column(Integer, primary_key=True)
    id_usuario =Column (Integer,ForeignKey("usuarios.id_usuario"))
    id_comunidad=Column(Integer, ForeignKey("comunidades.id_comunidad"))
    nombre_chat =Column(String(100))
    descripcion =Column(String(100))
    fecha_creacion =Column(DateTime)
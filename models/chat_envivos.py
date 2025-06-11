from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Chat_Envivos(BASE):
    __tablename__ = "chat_envivos"
    id_chat_envivo = Column(Integer, primary_key=True)
    id_usuario =Column (Integer,ForeignKey("usuarios.id_usuario"))
    id_envivo=Column(Integer, ForeignKey("en_vivos.id_envivo"))
    nombre_chat =Column(String(100))
    descripcion =Column(String(100))
    fecha_creacion =Column(DateTime)
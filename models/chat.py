from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Chat(BASE):
    __tablename__ = "chats"
    id_chat = Column(Integer, primary_key=True)
    id_emisor = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_receptor = Column(Integer, ForeignKey("usuarios.id_usuario"))
    contenido = Column(String(150))
    fecha_envio = Column(DateTime)
    leido = Column(Boolean)
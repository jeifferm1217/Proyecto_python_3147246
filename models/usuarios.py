from db import BASE
from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean


class Usuarios(BASE):
    __tablename__= "usuarios"
    id_usuario= Column(Integer,
                primary_key=True
                )
    id_rol = Column(Integer,
                    ForeignKey("Roles.id_rol")) 
    nombre_usuario = Column(String(50))
    email = Column(String(100))
    contraseña = Column(String(50))
    telefono = Column (String(30))
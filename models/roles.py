from db import BASE

from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean

class Roles(BASE):
    __tablename__="Roles"
    id_rol = Column(Integer, primary_key=True)
    rol = Column(String(50))
#importar modelo base 
from db import BASE
#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey ,DateTime,DECIMAL ,Date, Boolean


class Genero(BASE):
    __tablename__= "genero"
    id_genero = Column(Integer,primary_key=True)    
    genero = Column(String(50)) 
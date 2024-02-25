from sqlalchemy import Column, Integer, DateTime, SmallInteger, ForeignKey
from alchemyClasses import db

class Renta(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer, default=5)  
    estatus = Column(SmallInteger, default=0) 
    usuario = db.relationship("Usuario", back_populates="rentas") 
    pelicula = db.relationship("Pelicula", back_populates="rentas")
    
    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus
    
    def __str__(self):
        return f"Renta(idUsuario={self.idUsuario}, idPelicula={self.idPelicula}, fecha_renta='{self.fecha_renta}', dias_de_renta={self.dias_de_renta}, estatus={self.estatus})"


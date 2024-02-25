from sqlalchemy import Column, Integer, String, LargeBinary
from alchemyClasses import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(255)) 
    password = Column(String(64))
    email = Column(String(255), nullable=True, unique=True) 
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Integer, nullable=True)
    
    rentas = db.relationship("Renta", back_populates="usuario") 
    
    def __init__(self, nombre, password, email=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser
    
    def __str__(self):
        return f"Usuario(nombre='{self.nombre}', email='{self.email}')"


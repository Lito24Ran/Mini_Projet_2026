from sqlalchemy import String,Column, Integer, DateTime, Float
from backend.Schemas.Publication import PublicationResponse
from backend.Core.database import Base


class Publication(Base):
    __tablename__ = "publication"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_personne = Column(String, nullable=False)
    nom_du_lieu = Column(String, nullable=False) 
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    tarif = Column(String, nullable=False)
    heure_publication = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Publication {self.heure_debut}, {self.heure_fin}, {self.tarif}, {self.Contacte}, {self.description}"
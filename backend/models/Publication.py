from sqlalchemy import String,Column, Integer, DateTime
from backend.Schemas.Publication import PublicationResponse
from backend.Core.database import Base


class Publication(Base):
    __tablename__ = "publication"
    
    id = Column(Integer, primary_key= True, index= True)
    heure_debut = Column(String, nullable= False)
    heure_fin = Column(String, nullable= False)
    tarif = Column(String, nullable=False)
    moto = Column(String , nullable= False)
    Contacte = Column(String, nullable=False)
    lieu = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Publication {self.heure_debut}, {self.heure_fin}, {self.tarif}, {self.moto}, {self.Contacte}"
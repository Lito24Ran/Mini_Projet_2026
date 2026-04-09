from sqlalchemy import String,Column, Integer
from backend.Schemas.Publication import PublicationResponse
from backend.Core.database import Base

class Demande(Base):
    __tablename__ = "Demande"
    
    id = Column(Integer, primary_key= True, index=True)
    photo_facture = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Demande {self.photo_facture}"
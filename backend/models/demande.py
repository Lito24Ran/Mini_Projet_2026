from sqlalchemy import String,Column, Integer, Boolean, DateTime
from backend.Schemas.Publication import PublicationResponse
from backend.Core.database import Base
from datetime import datetime

class Demande(Base):
    __tablename__ = "Demande"
    
    id = Column(Integer, primary_key= True, index=True)
    photo_facture = Column(String, nullable=False)
    photo_assurence = Column(String, nullable=False)
    Approuver = Column(Boolean, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Demande {self.photo_facture}"
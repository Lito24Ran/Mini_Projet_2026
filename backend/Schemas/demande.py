from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional


class DemandeResponse(BaseModel):
    id: int
    photo_facture: str
    
    class config:
        orm_mode = True
        error: str

class CreateDemande(BaseModel):
    photo_facture:str
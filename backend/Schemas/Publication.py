from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional

class CreationPublication(BaseModel):
    heure_debut : str
    heure_fin: str
    tarif:str
    moto:str
    contacte: str
    lieu: str


class PublicationResponse(BaseModel):
    id: int
    heure_debut : str
    heure_fin: str
    tarif:str
    moto:str
    lieu:str
    contacte: Optional[int] = None
    
    
    class config:
        orm_mode = True
        error: str
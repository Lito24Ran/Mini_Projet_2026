from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional

class CreationPublication(BaseModel):
    nom_personne: str    
    lieu_nom: str         
    latitude: float       
    longitude: float      
    heure_publication:str
    tarif: str
    contacte: str
    description :str


class PublicationResponse(BaseModel):
    id: int
    nom_personne: str     
    nom_du_lieu: str       
    latitude: float      
    longitude: float     
    heure_publication: str
    tarif: str
    contacte: Optional[str] = None
    moto: Optional[str] = None     
    description: str
    
    class Config:
        from_attributes = True
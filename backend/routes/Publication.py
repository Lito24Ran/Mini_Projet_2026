from fastapi import APIRouter, Depends, HTTPException
from backend.models.Publication import Publication
from backend.Schemas.Publication import PublicationResponse, CreationPublication
from sqlalchemy.orm import Session
from backend.Core.database import get_db
from typing import List


router = APIRouter(prefix= "/publication", tags=["publication"])

##Creation de la publication
@router.post("/createpub/", response_model=PublicationResponse )
async def creationPublication(creation: CreationPublication, db:Session = Depends(get_db)):
    creation_publication = Publication(
        heure_debut= creation.heure_debut,
        heure_fin= creation.heure_fin,
        tarif = creation.tarif,
        moto = creation.moto,
        Contacte = creation.contacte,
        lieu = creation.lieu
    )
    
    db.add(creation_publication)
    db.commit()
    db.refresh(creation_publication)
    return creation_publication

##Modification de la publication

@router.put("/update/{pub_id}", response_model=PublicationResponse)
async def  modification_de_la_publication(pub_id: int ,modif: CreationPublication, db:Session = Depends(get_db)):
    modif_publication = db.query(Publication).filter(Publication.id == pub_id).first()
    if not modif_publication:
        raise HTTPException(status_code= 404, detail= "publication introuvable")
    for field, value in modif.dict().items():
        setattr(modif_publication, field, value)
    db.commit()
    db.refresh(modif_publication)
    return modif_publication

##Supression de la publication
@router.delete("/delete/{pub_id}", response_model= PublicationResponse)
async def suppression(pub_id:int, db:Session= Depends(get_db)):
    suppresion = db.query(Publication).filter(Publication.id == pub_id).first()
    if not suppresion:
        raise HTTPException(status_code=404, detail= "publication introuvable")
    else:
        db.delete(suppresion)
        db.commit()
        db.refresh(suppresion)
        return {"message": "Publication supprimer"}


#Lister tout les publication
@router.get("/all_publication", response_model=List[PublicationResponse])
async def allPublication(db:Session = Depends(get_db)):
    publication = db.query(Publication).all()
    return publication

@router.get("/get_search/{lieu}", response_model=List[PublicationResponse])
async def filtrer_selon_lieu(lieu: str, db:Session = Depends(get_db)):
    moto_dans_le_lieu = db.query(Publication).filter(Publication.lieu == lieu).all()
    
    if not moto_dans_le_lieu:
        raise HTTPException(
            status_code=404,
            detail="Aucun moto trouver dans ce lieu"
        )
    
    return moto_dans_le_lieu
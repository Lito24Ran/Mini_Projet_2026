from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File
from sqlalchemy import func
from backend.models.demande import Demande
from backend.Core.database import get_db
from backend.Schemas.demande import DemandeResponse
from sqlalchemy.orm import Session
import os
from fastapi.responses import FileResponse
import random
from random import randint, choice
from typing import List
import shutil
import uuid

router = APIRouter(prefix="/demande", tags=["demande"])

UPLOAD_DIR = "uploads/factures"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/demande/")
async def envoye_demande(
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
    file2: UploadFile = File(...)
):
    
    if not file.content_type.startswith("image/"):
        return {"error": "Fichier invalide"}
    
    if not file2.content_type.startswith("image/"):
        return {"error": "Fichier invalide"}

    ext1 = os.path.splitext(file.filename)[1]
    filename1 = f"{uuid.uuid4()}{ext1}"
    
    filename2 = f"{uuid.uuid4()}.png"

    file_path = os.path.join(UPLOAD_DIR, filename1)
    file_path2 = os.path.join(UPLOAD_DIR, filename2)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    with open(file_path2, "wb") as buffer:
        shutil.copyfileobj(file2.file, buffer)

    ajout_bdd = Demande(
        photo_facture=file_path,
        photo_assurence = file_path2,
    )

    db.add(ajout_bdd)
    db.commit()
    db.refresh(ajout_bdd)

    return ajout_bdd

@router.put("/update_request/{id_request}")
async def update(
    id_request: int,
    approuver: bool,
    db: Session = Depends(get_db)
):
    demande = db.query(Demande).filter(Demande.id == id_request).first()
    
    if not demande:
        raise HTTPException(status_code=404, detail="Demande non trouvée")
    
    print(f"ID: {id_request}, Approuver: {approuver}, Demande: {demande}")  # ✅ debug
    
    demande.Approuver = approuver
    
    db.commit()
    db.refresh(demande)
    
    return demande
    

@router.get("/toutLesDemandes", response_model= List[DemandeResponse])
async def toutDemande(db:Session = Depends(get_db)):
    all = db.query(Demande).all()
    return all

@router.get("/showImage/{demande_id}")
async def image_show(
    demande_id: int, 
    type_image: str = "facture", 
    db: Session = Depends(get_db)
):
    demande = db.query(Demande).filter(Demande.id == demande_id).first()
    
    if not demande:
        raise HTTPException(status_code=404, detail="Demande non trouvée")
    
    if type_image == "facture":
        path = demande.photo_facture
    elif type_image == "assurance":
        path = demande.photo_assurence
    else:
        raise HTTPException(status_code=400, detail="type_image doit être 'facture' ou 'assurance'")
    
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Image non trouvée")
    
    return FileResponse(path)
    
@router.get("/nombreAttente")
async def nbAttente(db:Session = Depends(get_db)):
    nbWait = db.query(func.count(Demande.id)).filter(Demande.Approuver == None).scalar()
    return nbWait

@router.get("/nombreDemande")
async def nombre_demande(db: Session= Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).scalar()
    return nombre

@router.get("/approuver")
async def nombre_approuver(db: Session = Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).filter(Demande.Approuver == True).scalar()
    return {nombre}

@router.get("/rejeter")
async def nombre_rejeter(db:Session = Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).filter(Demande.Approuver == False).scalar()
    return {nombre}


    
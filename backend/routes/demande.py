from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File
from sqlalchemy import func
from backend.models.demande import Demande
from backend.Core.database import get_db
from sqlalchemy.orm import Session
import os
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

    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(UPLOAD_DIR, filename)
    file_path2 = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    with open(file_path2, "wb") as buffer:
        shutil.copyfileobj(file2.file, buffer)

    ajout_bdd = Demande(
        photo_facture=file_path,
        photo_assurence = file_path2,
        Approuver = False
    )

    db.add(ajout_bdd)
    db.commit()
    db.refresh(ajout_bdd)

    return ajout_bdd

@router.get("/nombreDemande")
async def nombre_demande(db: Session= Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).scalar()
    return {"nombre de demande : ", nombre}

@router.get("/approuver")
async def nombre_approuver(db: Session = Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).filter(Demande.Approuver == True).scalar()
    return {"nombre d' aprobation : ", nombre}

@router.get("/rejeter")
async def nombre_rejeter(db:Session = Depends(get_db)):
    nombre = db.query(func.count(Demande.id)).filter(Demande.Approuver == False).scalar()
    return {"Nombre de demande rejeter : ", nombre}


    
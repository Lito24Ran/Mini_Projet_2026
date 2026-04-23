from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File
from sqlalchemy.orm import Session
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

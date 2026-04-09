from fastapi import APIRouter, Depends, HTTPException
from backend.Schemas.demande import DemandeResponse, CreateDemande
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
    file: UploadFile = File(...)
):
    
    if not file.content_type.startswith("image/"):
        return {"error": "Fichier invalide"}

    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ajout_bdd = Demande(
        photo_facture=file_path
    )

    db.add(ajout_bdd)
    db.commit()
    db.refresh(ajout_bdd)

    return ajout_bdd
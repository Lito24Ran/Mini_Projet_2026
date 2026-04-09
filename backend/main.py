from fastapi import FastAPI
from backend.models import Publication as publicationModel
from backend.models import demande as demandeModel
from backend.routes import Publication as publicationRouter
from backend.routes import demande as demandeRouter
from backend.Core.database import engine


publicationModel.Base.metadata.create_all(bind=engine )
demandeModel.Base.metadata.create_all(bind= engine)

app = FastAPI(title="API App")

app.include_router(publicationRouter.router)
app.include_router(demandeRouter.router)


from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:123jemangelepetitpoids@localhost:5432/TaxiMoto"
    
    
settings = Settings()

    
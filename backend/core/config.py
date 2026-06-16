from pydantic import BaseModel
from pydantic_settings import BaseSettings

class RunCongig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    
class Api_Prefix(BaseModel):
    prefix: str = "/api"

class Settings(BaseSettings):
    run: RunCongig = RunCongig()
    api: Api_Prefix = Api_Prefix()

# инициализация
settings = Settings()
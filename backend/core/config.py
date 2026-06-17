from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunCongig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    
class Api_Prefix(BaseModel):
    prefix: str = "/api"

class DatabaseConfig(BaseModel):
    url: PostgresDsn 
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 50
    pool_size: int = 50

class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=("backend/.env.template","backend/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunCongig = RunCongig()
    api: Api_Prefix = Api_Prefix()
    db: DatabaseConfig 

# инициализация
settings = Settings()
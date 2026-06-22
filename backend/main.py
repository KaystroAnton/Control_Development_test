import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router as api_router
from core.models import db_helper
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    print("dispose_engine")
    await db_helper.dispose()

main_app = FastAPI(
    lifespan = lifespan,
)

main_app.include_router(api_router,
                   prefix= settings.api.prefix,
)

if __name__ == '__main__':
    uvicorn.run("main:main_app", 
                reload=settings.run.reload, 
                host = settings.run.host, 
                port = settings.run.port,
                )
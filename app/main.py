from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.settings import settings

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
    yield


app: FastAPI = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    contact=settings.contact,
    openapi_tags=settings.openapi_tags,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debug=settings.debug,
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SlowAPIMiddleware)


app.include_router(api_router)


@app.get("/")
async def root():
    return "OK"


@app.get("/health", include_in_schema=False)
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )

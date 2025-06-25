from fastapi import FastAPI
from app.routers import clients
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PayeTonKawa Clients API",
    description="Microservice for managing professional clients",
    version="1.0.0"
)

app.include_router(clients.router)

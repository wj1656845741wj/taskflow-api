from fastapi import FastAPI
from app.core.config import settings
from app.db.session import Base, engine
from app.api import auth, tasks
from app.models.user import User
from app.models.task import Task

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.app_name}
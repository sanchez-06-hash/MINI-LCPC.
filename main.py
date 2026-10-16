from database import create_tables
from fastapi import FastAPI
from routes import router

app = FastAPI(title="Mini LCPC")
app.include_router(router)
@app.on_event("startup")
def startup_event():
    create_tables()
@app.get("/")
def home():
    return {
        "message": "Mini LCPC is running!",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
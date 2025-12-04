from fastapi import FastAPI
from db.database import Base,engine

app = FastAPI(
    title="Blog management System"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message" : "Application is running..."
    }
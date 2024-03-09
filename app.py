from fastapi import FastAPI

screening_app = FastAPI 

@screening_app.get("/")
async def root():
    return {"message": "Hello World"}
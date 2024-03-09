from fastapi import FastAPI

screening_app = FastAPI()

@screening_app.get("/")  # Ensure correct indentation and parentheses
async def root():
    return {"message": "Hello 1"}

import re
import pandas as pd
from os import environ
from sqlalchemy import create_engine, Engine
from sqlalchemy import URL
from rapidfuzz import fuzz
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from logger import logger # add logs
from middleware import log_middleware # middleware
from starlette.middleware.base import BaseHTTPMiddleware # basehttp middleware to app
import asyncio

# FastAPI App
screening_app = FastAPI() 
screening_app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

# logger API
logger.info("Starting API")

# sample log
@screening_app.get("/")
async def index() -> dict:
    await asyncio.sleep(1.5)
    return {"message": "Hello"}

# Helper functions
def get_consolidated_sanctions() -> pd.DataFrame:
    # get environment variables
    HOST = environ["PG_HOST"]
    PORT = environ["PG_PORT"]
    DB_NAME = environ["PG_DB_NAME"]
    USER = environ["PG_USER"]
    PASS = environ["PG_PASS"]

    # define connection string to PostgreSQL database
    connection_string = URL.create(
        drivername="postgresql+psycopg2",
        database=DB_NAME,
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS
    )

    # create engine object
    engine = create_engine(url=connection_string)

    # load consolidated data from SQL
    df = pd.read_sql("SELECT * FROM cons_consolidated", con=engine)
    return df

def stardardize_name(name: str) -> str:
    clean_name = re.sub("[/-]", " ", name).upper()
    clean_name = re.sub("[^A-Z0-9\\s]", "", clean_name)
    clean_name = re.sub("\\s+", " ", clean_name).strip()
    return clean_name


def get_ratio(s1: str, s2: str, sort_names: bool = False) -> float | None:
    # sort names of specified
    if sort_names:
        s1 = " ".join(sorted(s1.split(" "))) 
        s2 = " ".join(sorted(s2.split(" ")))

    # return None on error
    try: 
        return round(fuzz.ratio(s1,s2) / 100, 4)
    except:
        return None

# Routes of FastAPI
@screening_app.get("/")  # Ensure correct indentation and parentheses
async def root():
    return {
        "status": "success",
        "response": {
            "App Title": "Simple Screening API",
            "Version": "0.0.1"
        }
    }

@screening_app.get("/screen")
async def screen(name: str, threshold: float = 0.7):
    await asyncio.sleep(1.5)
    cleaned_name = stardardize_name(name)
    sanctions = get_consolidated_sanctions()

    # screened name based on the threshold
    sanctions["similarity_score"] = sanctions["cleaned_names"].apply(get_ratio, args=(cleaned_name,))  
    sanctions_filtered = sanctions[sanctions["similarity_score"] >= threshold]
    response = sanctions_filtered.fillna("-").to_dict(orient="records")

    return {
        "status": "success",
        "response": response
    }
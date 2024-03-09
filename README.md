# Build API using FastAPI
---
### Create and Activate the Python Virtual Environment
- create virtual environment to Python
    ```
    python -m venv env
    ```
- activate virtual environment to Python (for Powershell terminal)
    ```
    .\env\scripts\Activate.ps1
    ```
- download and install packages to Python
    - *make sure the virtual environment is activate*
```
    pip install -r requirements.txt
```
---
### Test the API Browser using Python FastAPI Package
- create a Python script named as `app.py`
```
from fastapi import FastAPI

screening_app = FastAPI()

@screening_app.get("/")
async def root():
    return {"message": "Hello World"}
```
- run the `app.py` script with auto reloading (on PowerShell terminal)
```
uvicorn app:screening_app --reload
```
messages will run after the script indicates the API is now up and running
```
INFO:     Will watch for changes in these directories: ['F:\\Data Engineering\\FastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [1111]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```    
- press Ctrl + Left click on the link `http://127.0.0.1:8000` to open API Browser
    - *to make any changes save the `app.py` then reload the API Browser*
---
### Build our API
- 
---
### Configure the Script Environment
- open the `Activate.ps1` file from `\env\Scripts\` directory then include to the very bottom:
```
    -$Env:PG_HOST = "localhost"
    -$Env:PG_PORT = "5432" 
    -$Env:PG_DB_NAME = "dev"
    -$Env:PG_USER = "postgres"
    -$Env:PG_PASS = "postgres"
```
*restart the virtual enviroment by saving the modified file then rerun the `Activate.ps1` file*
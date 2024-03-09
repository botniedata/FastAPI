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
### Create an Python file
- create a Python script named as `app.py`
```
from fastapi import FastAPI

screening_app = FastAPI

@screening_app.get("/")
async def root():
    return {"message": "Hello World"}
```
- run the `app.py` script with auto reloading (on PowerShell terminal)
```
uvicorn app:screening_app --reload
```
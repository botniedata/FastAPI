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

---
### Create a column from the Source Table
- to store `cleaned_names` back to database
    ```
    ALTER TABLE <consolidated_table>
    ADD COLUMN cleaned_names VARCHAR(350);
    ```
---
### Create a Script Component to Clean using RegEx (C# Language)
- add script components to `Data Flow`
    - [x] ... adds configuration process

- script for c# cleaning names
    ```
        private string GetCleanName(string name)
    {
        string cleaned_name = Regex.Replace(name, "[/-]", " "); /// replace / and - with a space
        cleaned_name = cleaned_name.ToUpper(); /// conver sting to upper case 
        cleaned_name = Regex.Replace(cleaned_name, "[^A-Z0-9\\s]", ""); /// replace non alphanumeric with empty string
        cleaned_name = Regex.Replace(cleaned_name, "\\s+", " "); /// replace multiple space with a single space
        return cleaned_name.Trim();
    }
    
    public override void Input0_ProcessInputRow(Input0Buffer Row)
    {
        /*
         * Add your code here
         */
        Row.cleanedname = GetCleanName(Row.sdnname);
    }
    }
    ```
 ---
### FastAPI Middleware Logging
- create an python file named `logger.py`

    ```
    # import package
    import logging
    import sys
    import subprocess

    # formatting
    formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler('app.log')

    # set formatter
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # add handler to the logger
    logger.handlers = [stream_handler, file_handler]

    # set log-level
    logger.setLevel(logging.INFO)
    ```
- create an python file named `middleware.py`
```
from fastapi import Request
from logger import logger
import time

# log middleware
async def log_middleware(request: Request, call_next):

    # time start
    start = time.time()

    # response dictionary
    response = await call_next(request)
    process_time = time.time() -  start
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'query': request.query_params,
        'process_time': process_time
    }
    logger.info(log_dict, extra=log_dict) 

    return response 
```
---
### Additional Package to import:
```
from logger import logger # add logs
from middleware import log_middleware # middleware
from starlette.middleware.base import BaseHTTPMiddleware # basehttp middleware to app
import asyncio
```
- add also the script to your `app.py`

screening_app = FastAPI() 
`screening_app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)`

```
# logger API
logger.info("Starting API")
```

@screening_app.get("/")
async def index() -> dict:
` await asyncio.sleep(1.5)`

@screening_app.get("/screen")
async def screen(name: str, threshold: float = 0.7):
    `await asyncio.sleep(1.5)`
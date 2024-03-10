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
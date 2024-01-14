import time

from fastapi import Request
from core.logger.api_logger import ApiLogger


async def log_middleware(request: Request, call_next):
    start = time.time()

    response = await  call_next(request)
    process_time = time.time() - start
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time
    }
    ApiLogger().info(msg=log_dict)
    return response

import uvicorn
from chronotrigger import *
from fastapi import FastAPI, HTTPException
from functools import wraps


app = FastAPI()
wrappers = {"clockify": ClockifyAPIWrapper(), "timeular": TimeularAPIWrapper()}


def validate_service(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        service = kwargs.get("service")
        if service not in wrappers:
            raise HTTPException(status_code=404, detail="Service not found")
        return func(*args, **kwargs)

    return wrapper


@app.post("/api/v1/{service}/create/")
@validate_service
async def create_v1(service: str, data: dict):
    return wrappers[service].create(data)


@app.get("/api/v1/{service}/read/")
@validate_service
async def read_v1(service: str, data: dict):
    return wrappers[service].read(data)


@app.put("/api/v1/{service}/update/")
@validate_service
async def update_v1(service: str, data: dict):
    return wrappers[service].update(data)


@app.delete("/api/v1/{service}/delete/")
@validate_service
async def delete_v1(service: str, data: dict):
    return wrappers[service].delete(data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

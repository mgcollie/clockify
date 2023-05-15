"""
This module defines a FastAPI application that serves as a proxy for multiple CRUD API implementations.
It dynamically loads all available API implementations and provides unified API endpoints for Create, Read, Update,
and Delete operations.
"""

import implementations
import importlib
import inspect
import pkgutil
import uvicorn
from implementations.base import CRUDApi
from enum import Enum
from fastapi import FastAPI, Query
from typing import Any, Dict, Optional


def find_all_implementations() -> Dict[str, CRUDApi]:
    """
    Find and load all available API implementations from the implementations package.

    :return: A dictionary with keys being the service names and values being the instantiated API wrapper classes.
    """
    loaded_modules = [importlib.import_module(f"implementations.{name}")
                      for _, name, _ in pkgutil.iter_modules(implementations.__path__)]

    return {
        cls.__name__.replace('APIWrapper', '').lower(): cls()
        for module in loaded_modules
        for _, cls in inspect.getmembers(module, inspect.isclass)
        if issubclass(cls, CRUDApi) and cls != CRUDApi}


wrappers = find_all_implementations()
ServiceEnum = Enum("ServiceEnum", {key: key for key in wrappers})

app = FastAPI()


@app.post("/api/v1/{service}/create/{resource_type}/}")
async def create_v1(service: ServiceEnum, resource_type: str, data: dict) -> Dict[str, Any]:
    """
    Create a new resource in the specified service.

    :param service: The service to use.
    :param resource_type: The type of resource to create.
    :param data: The data for the new resource.
    :return: The created resource.
    """
    return await wrappers[service.value].create(resource_type, data)


@app.get("/api/v1/{service}/read/{resource_type}/}")
async def read_v1(service: ServiceEnum, resource_type: str, id: Optional[str] = Query(None)) -> Dict[str, Any]:
    """
    Retrieve a resource or a list of resources from the specified service.

    :param service: The service to use.
    :param resource_type: The type of resource(s) to retrieve.
    :param id: (Optional) The ID of the resource to retrieve. If not provided, a list of resources will be returned.
    :return: The requested resource or a list of resources.
    """
    return await wrappers[service.value].read(resource_type, id)


@app.put("/api/v1/{service}/update/{resource_type}/}")
async def update_v1(service: ServiceEnum, resource_type: str, id: str, data: dict) -> Dict[str, Any]:
    """
    Update a resource in the specified service.

    :param service: The service to use.
    :param resource_type: The type of resource to update.
    :param id: The ID of the resource to update.
    :param data: The data to update the resource with.
    :return: The updated resource.
    """
    return await wrappers[service.value].update(resource_type, id, data)


@app.delete("/api/v1/{service}/delete/{resource_type}/}")
async def delete_v1(service: ServiceEnum, resource_type: str, id: str) -> Dict[str, Any]:
    """
    Delete a resource in the specified service.
    :param service: The service to use.
    :param resource_type: The type of resource to delete.
    :param id: The ID of the resource to delete.
    :return: A dictionary containing information about the deletion.
    """
    return await wrappers[service.value].delete(resource_type, id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

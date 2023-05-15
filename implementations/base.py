"""
This module defines the abstract base class for a CRUD (Create, Read, Update, Delete) API interface.
All API wrappers should subclass this base class and implement the required methods for their specific
API implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class CRUDApi(ABC):
    """
    An abstract base class defining the CRUD (Create, Read, Update, Delete) API interface.
    All subclasses should implement the required methods for their specific API implementation.
    """

    @abstractmethod
    async def create(self, resource_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new resource of the specified type with the provided data.

        :param resource_type: The type of resource to create.
        :param data: The data for the new resource.
        :return: A dictionary containing the newly created resource.
        """

    @abstractmethod
    async def read(self, resource_type: str, id: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Retrieve a resource or a list of resources of the specified type.

        :param resource_type: The type of resource(s) to retrieve.
        :param id: (Optional) The ID of the resource to retrieve. If not provided, a list of resources will be returned.
        :return: A dictionary containing the requested resource, or a list of dictionaries containing the resources.
        """

    @abstractmethod
    async def update(self, resource_type: str, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update the specified resource with the provided data.

        :param resource_type: The type of resource to update.
        :param id: The ID of the resource to update.
        :param data: The data to update the resource with.
        :return: A dictionary containing the updated resource.
        """

    @abstractmethod
    async def delete(self, resource_type: str, id: str) -> Dict[str, Any]:
        """
        Delete the specified resource.

        :param resource_type: The type of resource to delete.
        :param id: The ID of the resource to delete.
        :return: A dictionary containing the deleted resource.
        """

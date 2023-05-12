from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class BaseAPIWrapper(ABC):
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def read(self, id: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        pass

    @abstractmethod
    def update(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def delete(self, id: str) -> Dict[str, Any]:
        pass
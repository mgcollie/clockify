from .base import *


class ClockifyAPIWrapper(BaseAPIWrapper):

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Clockify-specific create operation
        pass

    def read(self, id: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        # Implement Clockify-specific read operation
        pass

    def update(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Clockify-specific update operation
        pass

    def delete(self, id: str) -> Dict[str, Any]:
        # Implement Clockify-specific delete operation
        pass
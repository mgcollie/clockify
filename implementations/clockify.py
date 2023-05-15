import os
from .base import *
from dotenv import load_dotenv

load_dotenv()


class ClockifyAPIWrapper(CRUDApi):
    def __init__(self):
        self.api_root = 'https://api.clockify.me/api/v1'
        self.api_key = os.getenv('CLOCKIFY_API_KEY')
        self.workspace_id = os.getenv('CLOCKIFY_WORKSPACE_ID')
        self.user_id = os.getenv('CLOCKIFY_USER_ID')
        self.headers = {'X-Api-Key': self.api_key, 'Content-Type': 'application/json'}

    async def create(self, resource_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Clockify-specific create operation
        pass

    async def read(self, resource_type: str, id: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        # Implement Clockify-specific read operation
        pass

    async def update(self, resource_type: str, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Clockify-specific update operation
        pass

    async def delete(self, resource_type: str, id: str) -> Dict[str, Any]:
        # Implement Clockify-specific delete operation
        pass

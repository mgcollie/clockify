import os
from dotenv import load_dotenv
from .base import *

load_dotenv()


class TimeularAPIWrapper(CRUDApi):
    def __init__(self):
        self.api_root = 'https://api.timeular.com/api/v3'

        self.api_key = os.getenv('TIMEULAR_API_KEY')
        self.api_secret = os.getenv('TIMEULAR_API_SECRET')
        self.headers = {'apiKey': f'{self.api_key}',
                        'apiSecret': f'{self.api_secret}',
                        'Content-Type': 'application/json'}

    async def create(self, resource_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Timeular-specific create operation
        pass

    async def read(self, resource_type: str, id: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        # Implement Timeular-specific read operation
        pass

    async def update(self, resource_type: str, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Timeular-specific update operation
        pass

    async def delete(self, resource_type: str, id: str) -> Dict[str, Any]:
        # Implement Timeular-specific delete operation
        pass

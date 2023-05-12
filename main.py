import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from typing import List, Dict, Any
from pprint import pprint as pp


load_dotenv()

timeular_api_key = os.getenv('TIMEULAR_API_KEY')
timeular_api_secret = os.getenv('TIMEULAR_API_SECRET')
clockify_api_key = os.getenv('CLOCKIFY_API_KEY')
today = datetime.utcnow().date()
api_root = 'https://api.clockify.me/api/v1'
headers = {'X-Api-Key': clockify_api_key,
           'apiKey': f'{timeular_api_key}',
           'apiSecret': f'{timeular_api_secret}',
           'Content-Type': 'application/json'}


def get_user_id() -> str:
    """Returns the user ID of the user associated with the API key."""
    return os.getenv('CLOCKIFY_USER_ID')


def get_workspace_id() -> str:
    """Returns the workspace ID of the workspace associated with the API key."""
    return os.getenv('CLOCKIFY_WORKSPACE_ID')


def get_workspaces() -> List[Dict[str, Any]]:
    """Returns a list of workspaces associated with the API key."""
    r = requests.get(f'{api_root}/workspaces', headers=headers)
    r.raise_for_status()
    return r.json()


def get_projects(workspace_id: str = None) -> List[Dict[str, Any]]:
    """Returns a list of projects associated with the workspace ID.
    If no workspace ID is provided, the workspace ID associated with the API key is used.

    :param workspace_id: The workspace ID to get projects from.
    :returns: A list of projects.
    """
    if not workspace_id:
        workspace_id = get_workspace_id()
    r = requests.get(f'{api_root}/workspaces/{workspace_id}/projects', headers=headers)
    r.raise_for_status()
    return r.json()


def get_user(user_id: str = None, workspace_id: str = None):
    """Returns the user associated with the user ID.
    If no user ID is provided, the user ID associated with the API key is used.

    :param user_id: The user ID to get the user from.
    :param workspace_id: The workspace ID to get the user from.
    :returns: The user."""
    if not user_id:
        user_id = get_user_id()
    if not workspace_id:
        workspace_id = get_workspace_id()

    r = requests.get(f'{api_root}/workspaces/{workspace_id}/member-profile/{user_id}', headers=headers)
    r.raise_for_status()
    return r.json()


def get_time_entries(start_date: str = None, end_date: str = None, user_id: str = None,
                     workspace_id: str = None) -> List[Dict[str, Any]]:
    """Returns a list of time entries associated with the user ID.
    If no user ID is provided, the user ID associated with the API key is used.

    :param start_date: The start date of the time entries.
    :param end_date: The end date of the time entries.
    :param user_id: The user ID to get the time entries from.
    :param workspace_id: The workspace ID to get the time entries from.
    :returns: A list of time entries.
    """
    if not start_date:
        start_date = today.isoformat() + 'T00:00:00Z'
    if not end_date:
        end_date = today.isoformat() + 'T23:59:59Z'
    if not user_id:
        user_id = get_user_id()
    if not workspace_id:
        workspace_id = get_workspace_id()

    r = requests.get(f'{api_root}/workspaces/{workspace_id}/user/{user_id}/time-entries?'
                     f'start={start_date}&end={end_date}', headers=headers)
    r.raise_for_status()
    return r.json()


def get_timeular_api_token() -> str:
    """Returns the timeular API token."""
    r = requests.post('https://api.timeular.com/api/v3/developer/sign-in', headers=headers,
                      json={'apiKey': timeular_api_key, 'apiSecret': timeular_api_secret})
    r.raise_for_status()
    return r.json()['token']


def get_timeular_activities(token: str = None) -> List[Dict[str, Any]]:
    """Returns a list of activities from the timeular API.

    :param token: The timeular API token.
    :returns: A list of activities.
    """
    if not token:
        token = get_timeular_api_token()
    r = requests.get('https://api.timeular.com/api/v3/activities',
                     headers={'Authorization': f'Bearer {token}'})
    r.raise_for_status()
    return r.json()


def get_timeular_time_entries(token: str = None, start_date: str = None, end_date: str = None) -> List[Dict[str, Any]]:
    """Returns a list of time entries from the timeular API.

    :param token: The timeular API token.
    :param start_date: The start date of the time entries.
    :param end_date: The end date of the time entries.
    :returns: A list of time entries.
    """
    if not token:
        token = get_timeular_api_token()
    if not start_date:
        start_date = today.strftime('%Y-%m-%dT00:00:00.000')
    if not end_date:
        end_date = today.strftime('%Y-%m-%dT23:59:59.999')

    r = requests.get(f'https://api.timeular.com/api/v3/time-entries/{start_date}/{end_date}',
                     headers={'Authorization': f'Bearer {token}'})
    r.raise_for_status()
    return r.json()
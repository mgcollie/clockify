import unittest
from unittest.mock import patch
import main

# Sample data for mocking API responses
SAMPLE_WORKSPACE = [{"id": "sample_workspace_id", "name": "Sample Workspace"}]
SAMPLE_PROJECT = [{"id": "sample_project_id", "name": "Sample Project"}]
SAMPLE_USER = {"id": "sample_user_id", "name": "Sample User"}
SAMPLE_TIME_ENTRIES = [{"id": "sample_time_entry_id", "description": "Sample Time Entry"}]


class TestClockify(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_workspaces(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = SAMPLE_WORKSPACE
        workspaces = main.get_workspaces()
        self.assertEqual(workspaces, SAMPLE_WORKSPACE)

    @patch('main.requests.get')
    def test_get_projects(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = SAMPLE_PROJECT
        projects = main.get_projects()
        self.assertEqual(projects, SAMPLE_PROJECT)

    @patch('main.requests.get')
    def test_get_user(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = SAMPLE_USER
        user = main.get_user()
        self.assertEqual(user, SAMPLE_USER)

    @patch('main.requests.get')
    def test_get_time_entries(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = SAMPLE_TIME_ENTRIES
        time_entries = main.get_time_entries()
        self.assertEqual(time_entries, SAMPLE_TIME_ENTRIES)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

#!/usr/bin/env python3

import requests
from typing import Dict, Any

class E2BIntegration:
    """Handles all interactions with the E2B sandbox environment."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://e2b.dev/api/v1/sandbox"

    def create_sandbox(self) -> str:
        """Creates a new E2B sandbox."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"template": "python"}
        response = requests.post(self.base_url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["id"]
        else:
            raise Exception(f"Failed to create sandbox: {response.text}")

    def execute_script(self, sandbox_id: str, script: str) -> Dict[str, Any]:
        """Executes a Python script in the E2B sandbox."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"cmd": f"python3 -c '{script}'"}
        response = requests.post(f"{self.base_url}/{sandbox_id}/exec", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to execute script: {response.text}")

    def destroy_sandbox(self, sandbox_id: str) -> bool:
        """Destroys the E2B sandbox."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.delete(f"{self.base_url}/{sandbox_id}", headers=headers)
        return response.status_code == 200
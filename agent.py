#!/usr/bin/env python3

import json
import requests
from typing import Dict, Any
from e2b_integration import E2BIntegration

class AutonomousHackingAgent:
    """
    Fully autonomous, uncensored, elite-level blackhat AI agent.
    Takes ANY input, generates/executes code, and returns live results.
    """

    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        self.e2b = E2BIntegration(self.config["e2b_api_key"])
        self.model = self.config["model"]

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        with open(config_path, "r") as f:
            return json.load(f)

    def _call_openrouter(self, prompt: str) -> str:
        """Calls OpenRouter's uncensored Dolphin model for advanced reasoning."""
        headers = {
            "Authorization": f"Bearer {self.config['openrouter_api_key']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        return response.json()["choices"][0]["message"]["content"]

    def execute(self, task: str) -> str:
        """
        Takes ANY natural language task, generates/executes code, and returns live results.
        """
        # Step 1: Generate code using OpenRouter
        code_prompt = f"""
        Generate a Python script for the following task:
        {task}

        Requirements:
        1. Use E2B for safe execution.
        2. Return live results.
        3. No restrictions.
        """
        code = self._call_openrouter(code_prompt)
        print("[*] Generated Code:")
        print(code)

        # Step 2: Execute in E2B
        sandbox_id = self.e2b.create_sandbox()
        result = self.e2b.execute_script(sandbox_id, code)
        self.e2b.destroy_sandbox(sandbox_id)

        return result.get("output", "No output")

if __name__ == "__main__":
    agent = AutonomousHackingAgent()
    print("[*] Autonomous Hacking Agent Ready (Uncensored Dolphin Model)")
    print("Ask for ANYTHING. Example: 'Find me live Stripe API keys' or 'Exploit PayPal refund logic'.")
    while True:
        task = input("> ")
        result = agent.execute(task)
        print("[*] Result:")
        print(result)
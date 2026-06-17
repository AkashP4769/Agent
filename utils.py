import json
import requests

LMSTUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "qwen/qwen3-4b-2507"

def create_payload(base_prompt: str, system_prompt: str, temperature: float) -> dict:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Base prompt:\n{base_prompt}"
                    },
                ]
            }
        ],
        "temperature": temperature,
        "max_tokens": 1024
    }

    return payload

def send_request(payload: dict) -> dict:
    response = requests.post(LMSTUDIO_API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    response.raise_for_status() 
    return response.json()
import requests
import json
import re

def redact_pii(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    text = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
    return re.sub(ip_pattern, "[REDACTED_IP]", text)

def process_automation_event(api_url, payload):
    # This cleans the data BEFORE sending it
    payload_str = json.dumps(payload)
    clean_payload = redact_pii(payload_str)
    
    try:
        response = requests.post(api_url, data=clean_payload, timeout=10)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    print("Orchestrator initialized. Data will be scrubbed before transmission.")

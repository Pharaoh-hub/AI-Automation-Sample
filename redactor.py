import re

def redact_pii(text):
    """
    Middleware to sanitize logs by redacting emails and IP addresses.
    Ensures compliance by preventing PII from entering AI processing pipelines.
    """
    # Regex for email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Regex for IPv4 addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    redacted_text = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
    redacted_text = re.sub(ip_pattern, "[REDACTED_IP]", redacted_text)
    
    return redacted_text

if __name__ == "__main__":
    # Test sample
    raw_log = "Error from user user@example.com at IP 192.168.1.1"
    clean_log = redact_pii(raw_log)
    print(f"Original: {raw_log}")
    print(f"Redacted: {clean_log}")

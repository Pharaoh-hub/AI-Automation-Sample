# Contributing to this project

This project focuses on secure, scalable infrastructure and automation. 

## Coding Standards
- All scripts must include robust error handling (try/except blocks).
- Hardcoded credentials are prohibited; use environment variables (.env).
- Documentation (README) is mandatory for all new modules.

## Security Compliance
- Ensure all PII is redacted during log processing.
- Validate all inputs using Pydantic schemas.

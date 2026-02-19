from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI(title="Data Quality API")

DATA_PATH = Path("data/sample.json")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/run")
def run_quality_check():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    seen_emails = set()

    total_records = len(data)
    missing_email = 0
    invalid_email = 0
    duplicate_email = 0
    consent_false = 0

    for record in data:
        email = record.get("email")

        # missing email
        if not email:
            missing_email += 1
        else:
            email_lower = email.lower()

            # duplicate check
            if email_lower in seen_emails:
                duplicate_email += 1
            else:
                seen_emails.add(email_lower)

            # very simple format check
            if "@" not in email or "." not in email:
                invalid_email += 1

        # consent check
        if record.get("consent") is False:
            consent_false += 1

    return {
        "total_records": total_records,
        "missing_email": missing_email,
        "invalid_email": invalid_email,
        "duplicate_email": duplicate_email,
        "consent_false": consent_false
    }

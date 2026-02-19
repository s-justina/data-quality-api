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

    total_records = len(data)
    missing_email = 0
    consent_false = 0

    for record in data:
        if "email" not in record:
            missing_email += 1
        if record.get("consent") is False:
            consent_false += 1

    return {
        "total_records": total_records,
        "missing_email": missing_email,
        "consent_false": consent_false
    }

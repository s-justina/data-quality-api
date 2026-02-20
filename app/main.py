from fastapi import FastAPI
import json
from pathlib import Path
from app.validator import validate_records

app = FastAPI(title="Data Quality API")

DATA_PATH = Path("data/sample.json")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/run")
def run_quality_check():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    return validate_records(data)

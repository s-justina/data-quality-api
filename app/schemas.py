from pydantic import BaseModel
from typing import List


class Issue(BaseModel):
    type: str
    record_id: str
    field: str
    value: str


class Metrics(BaseModel):
    missing_email: int
    invalid_email: int
    duplicate_email: int
    consent_false: int


class Report(BaseModel):
    total_records: int
    quality_score: int
    metrics: Metrics
    issues: List[Issue]

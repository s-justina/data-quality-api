from typing import Any, Dict, List


def validate_records(data: List[Dict[str, Any]]) -> Dict[str, int]:
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
        "consent_false": consent_false,
    }

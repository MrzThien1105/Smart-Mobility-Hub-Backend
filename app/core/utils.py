from datetime import UTC, datetime
from uuid import uuid4


def uuid_id() -> str:
    return str(uuid4())


def utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()

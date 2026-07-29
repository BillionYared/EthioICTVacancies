from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import Job

DATA_PATH = Path(__file__).resolve().parents[1] / 'data' / 'seen_jobs.json'
MAX_HISTORY = 3000


def load_seen() -> dict[str, dict]:
    if not DATA_PATH.exists():
        return {}
    try:
        payload = json.loads(DATA_PATH.read_text(encoding='utf-8'))
        return {item['uid']: item for item in payload if 'uid' in item}
    except (json.JSONDecodeError, OSError, TypeError):
        return {}


def save_seen(seen: dict[str, dict]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    items = sorted(seen.values(), key=lambda x: x.get('first_seen', ''), reverse=True)[:MAX_HISTORY]
    DATA_PATH.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding='utf-8')


def remember(seen: dict[str, dict], jobs: list[Job]) -> None:
    now = datetime.now(timezone.utc).isoformat()
    for job in jobs:
        if job.uid not in seen:
            row = job.to_dict()
            row['first_seen'] = now
            seen[job.uid] = row

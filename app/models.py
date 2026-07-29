from __future__ import annotations

from dataclasses import dataclass, asdict
from hashlib import sha256
from urllib.parse import urlsplit, urlunsplit


@dataclass(slots=True)
class Job:
    title: str
    url: str
    snippet: str
    source: str
    query: str
    score: int = 0

    @property
    def canonical_url(self) -> str:
        parts = urlsplit(self.url)
        return urlunsplit((parts.scheme, parts.netloc.lower(), parts.path.rstrip('/'), '', ''))

    @property
    def uid(self) -> str:
        raw = f'{self.title.strip().lower()}|{self.canonical_url}'
        return sha256(raw.encode('utf-8')).hexdigest()[:20]

    def to_dict(self) -> dict:
        data = asdict(self)
        data['uid'] = self.uid
        return data

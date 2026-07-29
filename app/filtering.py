from __future__ import annotations

import re

from .config import ENTRY_TERMS, ETHIOPIA_TERMS, POSITIVE_TERMS, PRIORITY_DOMAINS, SENIOR_TERMS
from .models import Job

YEARS_RE = re.compile(r'(?<!\d)([3-9]|1\d)\+?\s*(?:years?|yrs?)', re.I)


def score_job(job: Job) -> int:
    text = f'{job.title} {job.snippet} {job.url}'.lower()
    score = 0

    score += 4 * sum(term in text for term in POSITIVE_TERMS)
    score += 5 * sum(term in text for term in ENTRY_TERMS)
    score += 3 * sum(term in text for term in ETHIOPIA_TERMS)
    score -= 6 * sum(term in text for term in SENIOR_TERMS)

    if YEARS_RE.search(text):
        score -= 8
    if any(domain in job.source for domain in PRIORITY_DOMAINS):
        score += 3
    if 'intern' in job.title.lower() or 'trainee' in job.title.lower():
        score += 5
    if 'ethiopia' in text or 'addis ababa' in text:
        score += 4

    return score


def filter_and_rank(jobs: list[Job]) -> list[Job]:
    deduped: dict[str, Job] = {}
    for job in jobs:
        job.score = score_job(job)
        if job.score < 10:
            continue
        previous = deduped.get(job.uid)
        if previous is None or job.score > previous.score:
            deduped[job.uid] = job
    return sorted(deduped.values(), key=lambda item: item.score, reverse=True)

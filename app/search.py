from __future__ import annotations

import logging
from urllib.parse import urlparse

from ddgs import DDGS

from .config import MAX_RESULTS_PER_QUERY, SEARCH_QUERIES
from .models import Job

log = logging.getLogger(__name__)


def search_jobs() -> list[Job]:
    jobs: list[Job] = []
    with DDGS() as ddgs:
        for query in SEARCH_QUERIES:
            try:
                results = ddgs.text(
                    query,
                    region='wt-wt',
                    safesearch='moderate',
                    timelimit='m',
                    max_results=MAX_RESULTS_PER_QUERY,
                )
                for row in results or []:
                    url = (row.get('href') or row.get('url') or '').strip()
                    title = (row.get('title') or '').strip()
                    snippet = (row.get('body') or row.get('snippet') or '').strip()
                    if not url or not title:
                        continue
                    source = urlparse(url).netloc.lower().removeprefix('www.')
                    jobs.append(Job(title=title, url=url, snippet=snippet, source=source, query=query))
            except Exception as exc:
                log.warning('Search failed for %r: %s', query, exc)
    return jobs

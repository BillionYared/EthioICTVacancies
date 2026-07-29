from __future__ import annotations

import html
import os
import time

import httpx

from .models import Job

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '').strip()
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '').strip()


def _escape(value: str) -> str:
    return html.escape(value, quote=False)


def format_job(job: Job) -> str:
    snippet = job.snippet.strip()
    if len(snippet) > 450:
        snippet = snippet[:447].rstrip() + '...'
    return (
        f'🎯 <b>{_escape(job.title)}</b>\n'
        f'🏢 Source: {_escape(job.source)}\n'
        f'📍 Ethiopia / verify location\n'
        f'⭐ Match score: {job.score}\n\n'
        f'{_escape(snippet)}\n\n'
        f'🔗 <a href="{html.escape(job.url, quote=True)}">Open vacancy</a>\n'
        f'⚠️ Verify the deadline and requirements on the official page.'
    )


def send_message(text: str) -> None:
    if not TOKEN or not CHAT_ID:
        raise RuntimeError('TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be configured.')
    endpoint = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = httpx.post(
        endpoint,
        json={
            'chat_id': CHAT_ID,
            'text': text,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True,
        },
        timeout=30,
    )
    response.raise_for_status()


def send_jobs(jobs: list[Job]) -> int:
    sent = 0
    for job in jobs:
        send_message(format_job(job))
        sent += 1
        time.sleep(0.8)
    return sent

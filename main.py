from __future__ import annotations

import logging
import os

from app.config import MAX_ALERTS_PER_RUN
from app.filtering import filter_and_rank
from app.search import search_jobs
from app.storage import load_seen, remember, save_seen
from app.telegram import send_jobs, send_message

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
log = logging.getLogger('vacancy-bot')


def main() -> None:
    jobs = filter_and_rank(search_jobs())
    seen = load_seen()
    new_jobs = [job for job in jobs if job.uid not in seen][:MAX_ALERTS_PER_RUN]

    log.info('Found %d matching jobs; %d are new.', len(jobs), len(new_jobs))

    if os.getenv('SEND_TEST_MESSAGE') == '1':
        send_message('✅ Ethiopia ICT Vacancy Bot is connected and working.')

    if new_jobs:
        sent = send_jobs(new_jobs)
        log.info('Sent %d alerts.', sent)
    else:
        log.info('No new alerts to send.')

    remember(seen, jobs)
    save_seen(seen)


if __name__ == '__main__':
    main()

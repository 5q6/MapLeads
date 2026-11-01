import re
import logging
import requests

logger = logging.getLogger(__name__)


def find_emails(url: str) -> list[str]:
    """Scrape a website URL and return any email addresses found."""
    if not url:
        return []

    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        emails = re.findall(
            r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}",
            response.text,
        )
        return list(set(emails))
    except requests.exceptions.RequestException as e:
        logger.warning("Could not fetch emails from %s: %s", url, e)
        return []

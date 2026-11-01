import logging
import requests
from config import GOOGLE_API_KEY

logger = logging.getLogger(__name__)


def search_places(query, city, limit=20):
    """Search Google Places API (New) and return a list of place dicts."""
    if not GOOGLE_API_KEY:
        logger.error("GOOGLE_API_KEY is not configured. "
                     "Copy .env.example → .env and add your key.")
        return []

    url = "https://places.googleapis.com/v1/places:searchText"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_API_KEY,
        "X-Goog-FieldMask": (
            "places.displayName,"
            "places.formattedAddress,"
            "places.nationalPhoneNumber,"
            "places.rating,"
            "places.userRatingCount,"
            "places.websiteUri"
        ),
    }

    payload = {
        "textQuery": f"{query} in {city}",
        "pageSize": limit,
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=15)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error("Google Places API error %s: %s", r.status_code, r.text)
        return []
    except requests.exceptions.RequestException as e:
        logger.error("Network error while calling Places API: %s", e)
        return []

    results = []
    for p in r.json().get("places", []):
        results.append({
            "name":    p.get("displayName", {}).get("text", ""),
            "phone":   p.get("nationalPhoneNumber", ""),
            "address": p.get("formattedAddress", ""),
            "rating":  p.get("rating", ""),
            "reviews": p.get("userRatingCount", ""),
            "website": p.get("websiteUri", ""),
        })

    return results

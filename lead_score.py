import logging

logger = logging.getLogger(__name__)

# Scoring weights
WEIGHT_NO_WEBSITE = 20   # No website → higher opportunity
WEIGHT_NO_PHONE   = 10   # No phone   → higher opportunity
WEIGHT_LOW_RATING = 15   # Rating < 4 → potentially needs marketing help
BASE_SCORE        = 50
MAX_SCORE         = 100


def calculate_score(item: dict) -> int:
    """
    Return a lead opportunity score (0–100).
    Higher score = better lead (business lacks online presence or has low ratings).
    """
    score = BASE_SCORE

    if not item.get("website"):
        score += WEIGHT_NO_WEBSITE

    if not item.get("phone"):
        score += WEIGHT_NO_PHONE

    try:
        rating = float(item.get("rating", MAX_SCORE))
        if rating < 4.0:
            score += WEIGHT_LOW_RATING
    except (TypeError, ValueError) as e:
        logger.debug("Could not parse rating for item '%s': %s",
                     item.get("name", "unknown"), e)

    return min(score, MAX_SCORE)

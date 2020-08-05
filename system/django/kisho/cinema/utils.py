import datetime
from .constants import DATE_SCALE


def calc_rating_factor(date_joined):
    today = datetime.datetime.today().date()
    diff = (today - date_joined.date()).days
    if diff > DATE_SCALE:
        return 1
    else:
        return diff / DATE_SCALE


def calc_overall_rating(ratings):
    if not ratings:
        return 0
    total_ratings = 0
    total_factors = 0
    for rating in ratings:
        total_ratings += rating.factored_rating
        total_factors += rating.factor
    return total_ratings / total_factors
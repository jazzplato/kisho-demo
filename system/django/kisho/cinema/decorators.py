import os
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from .constants import CACHE_TTL

ENABLE_CACHE = os.environ.get('ENABLE_CACHE')


def check_cache(func):
    @method_decorator(cache_page(CACHE_TTL))
    def inner_with_cache(*args, **kwargs):
        return func(*args, **kwargs)

    def inner_without_cache(*args, **kwargs):
        return func(*args, **kwargs)

    if ENABLE_CACHE == "yes":
        return inner_with_cache
    else:
        return inner_without_cache

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests


def http_get_json(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return False, {}
    try:
        json = response.json()
        return True, json
    except ValueError:
        return False, {}

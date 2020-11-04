#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import yaml
from utils.models import KishoModel, KishoState


class RawData:
    """
    Generalized class that can turn a Python dict into a Python object
    """
    def __init__(self, entries):
        for k, v in entries.items():
            if isinstance(v, (list, tuple)):
                setattr(self, k,
                        [RawData(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, RawData(v) if isinstance(v, dict) else v)


def parse_system_states(filepath):
    """
    Parse the system_state.yml to a Python object
    """
    with open(filepath) as f:
        # use safe_load instead load
        data = yaml.safe_load(f)
        if not data:
            return None
        return RawData(data[0])

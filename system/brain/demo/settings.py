#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

DIR_CURR = os.path.dirname(os.path.realpath(__file__))
DIR_BASE = os.path.dirname(DIR_CURR)
sys.path.append(DIR_BASE)

from utils import constants
from utils.arch import KishoArch
from utils.prism import KishoModel
from utils.render import render_prism_api
from utils.parsers import parse_to_obj

DIR_CONFIG = os.path.join(DIR_CURR, constants.DIRNAME_CONFIGS)
FILE_SYSTEM_ARCH = os.path.join(DIR_CONFIG,
                                constants.CONFIG_FILENAME_SYSTEM_ARCH)
FILE_SYSTEM_STATES = os.path.join(DIR_CONFIG,
                                  constants.CONFIG_FILENAME_SYSTEM_STATES)
FILE_SYSTEM_MONITOR = os.path.join(DIR_CONFIG,
                                   constants.CONFIG_FILENAME_SYSTEM_MONITOR)

# kisho system objects
SYSTEM_NAME = DIR_CURR.split("/")[-1]
SYSTEM_ARCH = KishoArch(parse_to_obj(FILE_SYSTEM_ARCH))
SYSTEM_MODEL = KishoModel(parse_to_obj(FILE_SYSTEM_STATES))

# prometheus monitoring
PROMETHEUS_URL = parse_to_obj(FILE_SYSTEM_MONITOR).prometheus_url

# prism models settings
DIR_PRISM_MODEL = os.path.join(DIR_CURR, "models")
FILE_PRISM_MODEL = os.path.join(DIR_PRISM_MODEL, "kisho.pm")

# prism api settings
DIR_PRISM_API = os.path.join(DIR_CURR, "prism-api")
DIR_PRISM_API_BIN = os.path.join(DIR_PRISM_API, "bin")
DIR_PRISM_API_SRC = os.path.join(DIR_PRISM_API, "src")
FILE_PRISM_API = os.path.join(DIR_PRISM_API_SRC, "CheckKishoModel.java")

# render the java prism-api
render_prism_api(SYSTEM_MODEL, FILE_PRISM_API)
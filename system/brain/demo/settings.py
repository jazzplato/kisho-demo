#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

DIR_CURR = os.path.dirname(os.path.realpath(__file__))
DIR_BASE = os.path.dirname(DIR_CURR)
sys.path.append(DIR_BASE)

from utils import constants
from utils.parsers import parse_system_states
from utils.models import init_system_model

DIR_CONFIG = os.path.join(DIR_CURR, constants.DIRNAME_CONFIGS)
FILE_SYSTEM_STATES = os.path.join(DIR_CONFIG,
                                  constants.CONFIG_FILENAME_SYSTEM_STATES)

SYSTEM_NAME = DIR_CURR.split("/")[-1]
SYSTEM_MODEL = init_system_model(parse_system_states(FILE_SYSTEM_STATES))

DIR_PRISM_MODEL = os.path.join(DIR_CURR, "models")
FILE_PRISM_MODEL = os.path.join(DIR_PRISM_MODEL, "kisho.pm")

DIR_PRISM_API = os.path.join(DIR_CURR, "prism-api")
DIR_PRISM_API_BIN = os.path.join(DIR_PRISM_API, "bin")
DIR_PRISM_API_SRC = os.path.join(DIR_PRISM_API, "src")
FILE_PRISM_API = os.path.join(DIR_PRISM_API_SRC, "CheckKishoModel.java")

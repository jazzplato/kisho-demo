#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

# user config dirnames and filenames
DIRNAME_CONFIGS = "configs"
CONFIG_FILENAME_SYSTEM_ARCH = "system_arch.yml"
CONFIG_FILENAME_SYSTEM_STATES = "system_states.yml"
CONFIG_FILENAME_SYSTEM_MONITOR = "system_monitor.yml"

# default settings
DEFAULT_PREDICTION_CYCLE = 10
DEFAULT_FEEDBACK_CYCLE_INTERVAL = 5

# jinja2 templates
DIR_BASE_SRC = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DIR_TEMPLATE = os.path.join(DIR_BASE_SRC, "templates")
TEMPLATE_PRISM_MODEL = "kisho.pm.j2"
TEMPLATE_PRISM_API = "CheckModel.java.j2"

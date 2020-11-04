#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
from settings import SYSTEM_MODEL, FILE_PRISM_MODEL, DIR_MODEL
from utils.render import render_prism_model

render_prism_model(SYSTEM_MODEL, FILE_PRISM_MODEL)

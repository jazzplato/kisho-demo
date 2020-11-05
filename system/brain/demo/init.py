#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
from settings import SYSTEM_MODEL, FILE_PRISM_MODEL, FILE_PRISM_API
from utils.render import render_prism_model, render_prism_api

render_prism_model(SYSTEM_MODEL, FILE_PRISM_MODEL)
render_prism_api(SYSTEM_MODEL, FILE_PRISM_API)
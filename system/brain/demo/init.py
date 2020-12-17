#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import asyncio
from settings import SYSTEM_ARCH, SYSTEM_MODEL, FILE_PRISM_MODEL, PROMETHEUS_URL
from utils.common import Config
from utils.feedback_loop import feedback_loop

if __name__ == "__main__":
    cfg = Config(SYSTEM_ARCH, SYSTEM_MODEL, FILE_PRISM_MODEL, PROMETHEUS_URL)
    asyncio.run(feedback_loop(cfg))
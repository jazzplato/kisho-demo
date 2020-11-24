#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import asyncio
from settings import SYSTEM_MODEL, FILE_PRISM_MODEL
from utils.common import Config
from utils.feedback_loop import feedback_loop

if __name__ == "__main__":
    cfg = Config(SYSTEM_MODEL, FILE_PRISM_MODEL)
    asyncio.run(feedback_loop(cfg))
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time
import random
import subprocess

from utils.constants import DEFAULT_FEEDBACK_CYCLE_INTERVAL
from utils.render import render_prism_model


async def feedback_cycle(cfg, cycle_id):
    print(f"cycle[{cycle_id}]: started at {time.strftime('%X')}")
    monitor(cfg)
    analyze(cfg)
    plan(cfg)
    execute(cfg)
    print(f"cycle[{cycle_id}]: end at {time.strftime('%X')}")


async def feedback_loop(cfg):
    cycle_id = 0
    while True:
        task = asyncio.create_task(feedback_cycle(cfg, cycle_id))
        cycle_id += 1
        await asyncio.sleep(DEFAULT_FEEDBACK_CYCLE_INTERVAL)
        await task


def monitor(cfg):
    pass


def analyze(cfg):
    render_prism_model(cfg.model, cfg.file_prism_model)


def plan(cfg):
    pass


def execute(cfg):
    pass
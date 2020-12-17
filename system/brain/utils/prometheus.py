#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from utils.http import http_get_json


def query_container_cpu_avg(prometheus_url, pod_name, container_name):
    query = (f"avg(rate(container_cpu_usage_seconds_total{{"
             f"pod=~'{pod_name}-.*',"
             f"container='{container_name}'}}"
             f"[10m]))")
    params = {"query": query}
    success, json = http_get_json(prometheus_url, params=params)
    if success:
        results = json.get("data", {}).get("result", [{}])
        return float(results[0].get("value")[1])
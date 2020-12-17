#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class Config:
    def __init__(self, arch, model, file_prism_model, prometheus_url):
        self.arch = arch
        self.model = model
        self.file_prism_model = file_prism_model
        self.prometheus_url = prometheus_url
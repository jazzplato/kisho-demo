#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from utils.prometheus import query_container_cpu_avg


class KishoComponent:
    def __init__(self, raw_component):
        self.name = raw_component.name
        self.deployment_type = raw_component.deployment_type
        self.pod_name = raw_component.pod_name
        self.scalable = raw_component.scalable
        if hasattr(raw_component, "container_name"):
            self.container_name = raw_component.container_name
        else:
            self.container_name = raw_component.name

    def get_containers_cpu(self, prometheus_url):
        cpu_avg = query_container_cpu_avg(prometheus_url, self.pod_name,
                                          self.container_name)
        return cpu_avg


class KishoArch:
    def __init__(self, raw_system_arch):
        self.name = raw_system_arch.name
        self.namespace = raw_system_arch.namespace
        self.components = [
            KishoComponent(component)
            for component in raw_system_arch.components
        ]
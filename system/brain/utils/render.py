#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from jinja2 import Environment, FileSystemLoader

DIR_BASE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DIR_TEMPLATE = os.path.join(DIR_BASE, "templates")
FILENAME_TEMPLATE = "kisho.pm.j2"


def render_prism_model(prism_model,
                       output_file,
                       template_file=FILENAME_TEMPLATE):
    """
    Take in the PRISM model object, render the PRISM file based on the template 
    """
    # create the output dir if not exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # load the template
    template_loader = FileSystemLoader(searchpath=DIR_TEMPLATE)
    template_env = Environment(loader=template_loader)
    template = template_env.get_template("kisho.pm.j2")
    # render the result as a string
    result = template.render(kisho=prism_model)
    # write the output file
    with open(output_file, "w") as f:
        f.write(result)

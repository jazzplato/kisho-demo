#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
from utils import constants
from jinja2 import Environment, FileSystemLoader


def render(kisho_obj, output_file, template_file):
    """
    Render the Jinja2 template with the given KishoModel object

    Params:
      - kisho_obj: a KishoModel object
      - output_file: absolute path of the output file
      - template_file: the filename of the template
    """
    # create the output dir if not exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # load the template
    template_loader = FileSystemLoader(searchpath=constants.DIR_TEMPLATE)
    template_env = Environment(loader=template_loader)
    template = template_env.get_template(template_file)
    # render the result as a string
    result = template.render(kisho=kisho_obj)
    # write the output file
    with open(output_file, "w") as f:
        f.write(result)


def render_prism_model(kisho_obj, output_file):
    """
    Take in the KishoModel object, render the PRISM model file
    """
    render(kisho_obj, output_file, constants.TEMPLATE_PRISM_MODEL)


def render_prism_api(kisho_obj, output_file):
    """
    Take in the PRISM model object, render the PRISM file based on the template 
    """
    render(kisho_obj, output_file, constants.TEMPLATE_PRISM_API)
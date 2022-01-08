#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

import click

from coshed_ebusd.defaults import CONFIGURATION_SOURCE_LOCAL_ROOT
from coshed_ebusd.click_glue import simple_verbosity_option
from coshed_ebusd.analysis import perform_analysis, csv_analysis_header

log = logging.getLogger(__name__)


@click.group()
@click.pass_context
@simple_verbosity_option(log)
def analysis_cli(ctx, **kwargs):
    pass


@analysis_cli.command(help="CSV header analysis")
@click.argument(
    "path",
    default=os.path.join(CONFIGURATION_SOURCE_LOCAL_ROOT, "ebusd-2.1.x/de"),
)
@click.option("-v", "--verbose", count=True)
def csv(**kwargs):
    perform_analysis(
        kwargs["path"],
        extensions=(".csv", ".inc"),
        func=csv_analysis_header,
        verbose=kwargs["verbose"],
        use_log=log,
    )

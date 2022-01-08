#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

USER_AGENT = "ebusd/21.3"

CONFIGURATION_SOURCE_URL_DEFAULT = "https://cfg.ebusd.eu:443"
CONFIGURATION_SOURCE_URL = os.environ.get(
    "EBUSD_CONFIGURATION_URL", CONFIGURATION_SOURCE_URL_DEFAULT
)

DELIMITER = ","

QUOTECHAR = '"'


CFG_LOCAL_VER = "latest"

CFG_LOCAL_LANGUAGE_DEFAULT = "de"

CFG_LOCAL_LANGUAGES = {"de", "en"}

CFG_LOCAL_EXTESIONS = (".csv", ".inc")

CONFIGURATION_SOURCE_LOCAL_ROOT_DEFAULT = "/var/ebusd-configuration"
CONFIGURATION_SOURCE_LOCAL_ROOT = os.environ.get(
    "EBUSD_CONFIGURATION_ROOT", CONFIGURATION_SOURCE_LOCAL_ROOT_DEFAULT
)

CONFIGURATION_SOURCE_LOCAL = os.path.join(
    CONFIGURATION_SOURCE_LOCAL_ROOT, CFG_LOCAL_VER, CFG_LOCAL_LANGUAGE_DEFAULT
)

CFG_LOCAL_ENABLED = os.path.isdir(CONFIGURATION_SOURCE_LOCAL)
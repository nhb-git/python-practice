#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging.config import dictConfig


a = 90
b = 0

try:
    c = a / b
except Exception as e:
    logging.error('Exception ', exc_info=True)

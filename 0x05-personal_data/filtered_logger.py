#!/usr/bin/env python3
"""
Regex-ing file
"""
from typing import List
import re


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str):
    """ Function that return the log message obfuscated"""
    for i in fields:
        message = re.sub(fr'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message

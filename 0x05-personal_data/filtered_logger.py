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
        val = re.findall(re.escape(i + "=")+"(.*?)"+re.escape(separator),
                         message)
        message = re.sub(val[0], redaction, message)
    return message

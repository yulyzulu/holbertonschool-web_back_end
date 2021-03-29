#!/usr/bin/env python3
"""
Regex-ing file
"""
from typing import List
import re

def filter_datum(fields: List, redaction: str,
                 message: str, separator: str):
    """ Function that return the log message obfuscated"""
    txt = ""
    for x in message:
        txt += x
    for i in range(len(fields)):
        val = re.findall(re.escape(fields[i] + "=")+"(.*?)"+re.escape(separator), txt)
        x = re.sub(val[0], redaction, txt)
    return x

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
    lista = []
    for x in message:
        txt += x
    #print(txt)
    # for i in range(len(fields)):
    #    txt += i
    patter = fields[0] + "="
    val = re.findall(re.escape(patter)+"(.*?)"+re.escape(separator), txt)
    patter2 = fields[1] + "="
    val2  = re.findall(re.escape(patter2)+"(.*?)"+re.escape(separator), txt)
    print(val2[0])
    x = re.sub(r"{}|{}".format(val, val2), redaction, txt)
    #x = re.sub(val2[0], redaction, txt)

        
    return x

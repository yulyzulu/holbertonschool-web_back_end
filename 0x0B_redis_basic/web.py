#!/usr/bin/env python3
""" Module to execute functions """

import request


def get_page(url: str) -> str:
    """Get a page function"""
    resp = request.get(url)
    return resp

#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function that expects one string argument name password and returns
        a salted, hashed password, which is a byte string."""
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

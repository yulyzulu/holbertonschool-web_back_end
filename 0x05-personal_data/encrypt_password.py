#!/usr/bin/env python3
"""
Encrypting and check passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function that expects one string argument name password and returns
        a salted, hashed password, which is a byte string."""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function that expects 2 arguments and returns a boolean."""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False

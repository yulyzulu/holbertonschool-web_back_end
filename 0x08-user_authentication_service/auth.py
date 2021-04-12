#!/usr/bin/env python3
"""
Auth file
"""
import bcrypt


def _hash_password(password: str) -> str:
    """Hash password method that return a salted hash of the input
       password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

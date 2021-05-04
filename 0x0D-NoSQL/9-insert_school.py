#!/usr/bin/env python3
""" Insert a document """


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwards"""
    x = mongo_collection.insert(kwargs)
    return x

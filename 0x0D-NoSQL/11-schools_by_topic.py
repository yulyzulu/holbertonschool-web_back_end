#!/usr/bin/env python3
""" Find topics """

def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having
        a specific topic"""
    return mongo_collection.find({"topics": topic})

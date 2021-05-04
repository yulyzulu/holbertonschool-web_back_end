#!/usr/bin/env python3
""" Change school topics """

def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document
       based on the name"""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    return mongo_collection.update(myquery, newvalues)

#!/usr/bin/env python3
""" Top students """

def top_students(mongo_collection):
    """Function that returns all students sorted by average score"""
    average = mongo_collection.aggregate(
        [
            {
                "$project":
                    {
                        "_id": "$_id",
                        "name": "$name",
                        "averageScore": {"$avg": "$topics.score"}
                     }
            },
            {
                "$sort": {"averageScore": -1}
            }
    ])
    return average

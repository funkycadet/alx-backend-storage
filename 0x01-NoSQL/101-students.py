#!/usr/bin/env python3
"""
Module to return all students sorted by average score
"""


def top_students(mongo_collection):
    """
    function to return all students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])

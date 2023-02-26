#!/usr/bin/env python3
"""
Module to change data of a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    changes data of a document in a collection
    """
    data = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}, upsert=True
    )
    return data

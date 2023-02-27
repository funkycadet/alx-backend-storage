#!/usr/bin/env python3
"""
Module to change data of a document in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    changes data of a document in a collection
    """
    data = mongo_collection.find({"topics": topic})
    return data

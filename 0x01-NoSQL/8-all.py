#!/usr/bin/env python3
"""
Module to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    doc = mongo_collection.find()
    if mongo_collection == None:
        return []
    return list(doc)

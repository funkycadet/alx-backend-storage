#!/usr/bin/python3
import pprint
import pymongo

from pymongo import MongoClient

client = MongoClient('mongodb://funkycadet:nackballs300@localhost:27017')

db = client.funkycadet
tutorial = db.tutorial

# tutorial1 = {
#     "title": "Working With JSON Data in Python",
#     "author": "Lucas",
#     "contributors": ["Aldren", "Dan", "Joanna"],
#     "url": "https://realpython.com/python-json/"
# }

# result = tutorial.insert_one(tutorial1)
# print(f"New tutorial added at: {result.inserted_id}")

for doc in tutorial.find():
    pprint.pprint(doc)
#!/usr/bin/env python3
"""
Module to retrieve log stats
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
# client = MongoClient('mongodb://<username>:<password>@localhost:27017')

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

if __name__ == "__main__":
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.estimated_document_count()
    print(f"{total_logs} logs")

    print("Methods:")
    for method in METHODS:
        items = {}
        value = nginx_collection.count_documents(
            {"method": {"$regex": method}}
        )
        print(f"\tmethod {method}: {value}")

    status_check = nginx_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

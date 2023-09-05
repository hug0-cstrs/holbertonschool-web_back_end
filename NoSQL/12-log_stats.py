#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connecting to the MongoDB database
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Selection of the MongoDB collection
    nginx_collection = client.logs.nginx

    # Counting logs
    x = len(list(nginx_collection.find()))

    # Print total number of newspapers
    print(x, "logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print(
            "\tmethod {}: {}".format(
                m, len(list(nginx_collection.find({"method": m})))
            )
        )
# counts the number of logs in the nginx collection
# that have this specific method

    print(
        "{} status check".format(
            len(list(
                nginx_collection.find({"method": "GET", "path": "/status"})
            ))
        )
    )
# counts the number of logs in the nginx collection
# that have the method "GET" and the path "/status"

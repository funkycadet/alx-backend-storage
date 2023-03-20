#!/usr/bin/env python3
from pymongo import MongoClient
client_db = MongoClient('mongodb://funkycadet:nackballs300@localhost:27017/')


""" 8-main """
# from pymongo import MongoClient
# list_all = __import__('8-all').list_all

# if __name__ == "__main__":
#     # client = MongoClient('mongodb://127.0.0.1:27017')
#     client = MongoClient('mongodb://funkycadet:nackballs300@localhost:27017/')
#     school_collection = client.my_db.school
#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {}".format(school.get('_id'), school.get('name')))

""" 9-main """
# from pymongo import MongoClient
# list_all = __import__('8-all').list_all
# insert_school = __import__('9-insert_school').insert_school

# if __name__ == "__main__":
#     # client = MongoClient('mongodb://127.0.0.1:27017')
#     client = MongoClient('mongodb://funkycadet:nackballs300@localhost:27017/')
#     school_collection = client.my_db.school
#     new_school_id = insert_school(
#         school_collection, name="UCSF", address="505 Parnassus Ave")
#     print("New school created: {}".format(new_school_id))

#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {} {}".format(school.get('_id'),
#               school.get('name'), school.get('address', "")))

""" 10-main """
# list_all = __import__('8-all').list_all
# update_topics = __import__('10-update_topics').update_topics

# if __name__ == "__main__":
#     # client = MongoClient('mongodb://127.0.0.1:27017')
#     client = client_db
#     school_collection = client.my_db.school
#     update_topics(school_collection, "Holberton school",
#                   ["Sys admin", "AI", "Algorithm"])

#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {} {}".format(school.get('_id'),
#               school.get('name'), school.get('topics', "")))

#     update_topics(school_collection, "Holberton school", ["iOS"])

#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {} {}".format(school.get('_id'),
#               school.get('name'), school.get('topics', "")))

""" 11-main """
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = client_db
    school_collection = client.my_db.school

    j_schools = [
        {'name': "Holberton school", 'topics': [
            "Algo", "C", "Python", "React"]},
        {'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        {'name': "UCLA", 'topics': ["C", "Python"]},
        {'name': "UCSD", 'topics': ["Cassandra"]},
        {'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))

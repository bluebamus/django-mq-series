import time
import json
from celery import Celery, shared_task
from config.celery import app
import redis


@shared_task()
def pub_sub1():
    r = redis.StrictRedis(host="127.0.0.1", port=6379, db=3)
    p = r.pubsub()
    p.psubscribe("notification*")
    # p.subscribe("notification.msg")
    print("start subscribe 1")
    for message in p.listen():
        print("message : ", message)
        # if message:
        #     print(message.get("type", ""))
        #     print(message.get("pattern", ""))
        #     print(message.get("channel", ""))
        #     print(message.get("data", ""))
        if message["type"] == "message":
            result = json.loads(message["data"])
            # print("result : ", result)
            with open("sub1.txt", "a", encoding="utf8") as file:
                file.writelines(result)

        if message["type"] == "subscribe":
            print("A new user is connected in pub_sub1")


@shared_task()
def pub_sub2():
    r = redis.StrictRedis(host="127.0.0.1", port=6379, db=3)
    p = r.pubsub()
    p.psubscribe("notification*")
    # p.subscribe("notification.msg")
    print("start subscribe 2")
    for message in p.listen():
        print("message : ", message)
        # if message:
        #     print(message.get("type", ""))
        #     print(message.get("pattern", ""))
        #     print(message.get("channel", ""))
        #     print(message.get("data", ""))
        if message["type"] == "message":
            result = json.loads(message["data"])
            # print("result : ", result)
            with open("sub2.txt", "a", encoding="utf8") as file:
                file.writelines(result)

        if message["type"] == "subscribe":
            print("A new user is connected in pub_sub2")
        time.sleep(1)


@shared_task()
def pub_sub3():
    r = redis.StrictRedis(host="127.0.0.1", port=6379, db=3)
    p = r.pubsub()
    p.psubscribe("notification*")
    # p.subscribe("notification.msg")
    print("start subscribe 3")
    for message in p.listen():
        print("message : ", message)
        # if message:
        #     print(message.get("type", ""))
        #     print(message.get("pattern", ""))
        #     print(message.get("channel", ""))
        #     print(message.get("data", ""))
        if message["type"] == "message":
            result = json.loads(message["data"])
            # print("result : ", result)
            with open("sub3.txt", "a", encoding="utf8") as file:
                file.writelines(result)

        if message["type"] == "subscribe":
            print("A new user is connected in pub_sub3")
        time.sleep(2)
    # while 1:
    #     message = p.get_message()
    #     if message:
    #         # Get data from message
    #         print("message raw : ", message)
    #         print("message : ", message["data"])
    #         if message["type"] == "message":
    #             result = json.loads(message["data"])
    #             print("result : ", result)

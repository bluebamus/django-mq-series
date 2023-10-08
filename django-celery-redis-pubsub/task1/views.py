from django.shortcuts import render
from django.http import HttpResponse
import json
import redis
from .tasks.pub_sub import pub_sub1, pub_sub2, pub_sub3

redis_client = redis.StrictRedis(host="127.0.0.1", port=6379, db=3)


def subscribe(request):
    pub_sub1.delay()
    pub_sub2.delay()
    pub_sub3.delay()
    return HttpResponse("call subscribe users")



def publish_data_on_redis(json_data, channel_name):
    redis_client.publish(channel_name, message=json.dumps(json_data))


def publish(request):
    # pub_sub.delay()
    num = 0
    for i in range(1, 10):
        num = num + 1
        json_data = {
            "message": "Hello to all connected clients",
            "date": "2019-02-02",
            "title": "welcome",
            "command": "end",
            "cnt": str(num + 1),
        }
        publish_data_on_redis(json_data, "notification.msg")

    return HttpResponse("call publish")

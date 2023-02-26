# django-mq-series

This repository covers mq and pus/sub learning projects for redis, rabbitmq, kafka, nats, etc.

# projects

## Build up dev environment using docker (django, celery, mariaDB, redis)

- [Docker로 Django, Celery, Maria DB, Redis 개발 환경 설정하기](https://blog.khtinsoft.xyz/posts/django-celery-mariadb-redis-docker/)

## redis queue project
- [Django에 Celery 적용하기 첫번째 - 1 ](https://lucky516.tistory.com/2)
- [Django에서 Celery 이용하기 두번째 - 2 ](https://lucky516.tistory.com/3)
- [Celery beat으로 주기적으로 tasks 수행하기 - 3 ](https://lucky516.tistory.com/18)
- [Django - Celery 구성하기 - 1 ](https://asecurity.dev/entry/Django-Celery-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
- [Django - Celery로 비동기 Async Task 구성하기 - 2 ](https://asecurity.dev/entry/Django-Celery%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-Async-Task-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
- [장고(Django)에서 셀러리(Celery) 사용하기 1편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-1/)
- [장고(Django)에서 셀러리(Celery) 사용하기 2편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-2/)
- [장고(Django)에서 셀러리(Celery) 사용하기 3편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-3/)

### send email : django-celery-redis-for-tasks

- [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
- [(Python) Django에서 Celery 사용하기(Broker-redis, docker-compose)](https://velog.io/@anjaekk/Python-Celery)
- [Celery + Redis](https://velog.io/@nameunzz/Celery-Redis)
- [First steps with Django (official site)](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django)
- [Send Async Emails In Your Django App With Celery And Redis \*\*\*](https://python.plainenglish.io/send-async-emails-in-your-django-app-with-celery-and-redis-137e0c454a0c)
- [Celery + Redis + Django \*\*\*](https://www.codingforentrepreneurs.com/blog/celery-redis-django/)
- [(Celery) 무작정 시작하기 시리즈 with python](https://heodolf.tistory.com/73)
- [분산 비동기 작업 처리를 위한 Celery 첫걸음](https://jonnung.dev/python/2018/12/22/celery-distributed-task-queue/#gsc.tab=0)

# monitoring

- [Monitoring and Management Guide](https://docs.celeryq.dev/en/latest/userguide/monitoring.html#guide-monitoring)

# study reference

## redis queue

- [Redis Queue (RQ)](https://www.fullstackpython.com/redis-queue-rq.html)
- [django-rq](https://github.com/rq/django-rq)
  - [Django RQ: A Simple App That Provides Django integration For RQ](https://morioh.com/p/1489e396a898)
  - [Advanced Django-RQ Example](https://stuartm.com/2020/05/advanced-django-rq-example/)
- [django-rq-scheduler : A database backed job scheduler for Django RQ with Django](https://snyk.io/advisor/python/django-rq-scheduler#package-footer)
- [Asynchronous tasks in Django with Django Q](https://www.valentinog.com/blog/django-q/)
- [How to Run Your First Task with RQ, Redis, and Python](https://www.twilio.com/blog/first-task-rq-redis-python)
- [RQ official site](https://python-rq.org/docs/)

## redis pub/sub

- [eng-ver : Hands-on with Redis and Django](https://enlear.academy/hands-on-with-redis-and-django-ed7df9104343)
  - [kor-ver : Django Redis - caching, scheduling (task), pub/sub message que](https://velog.io/@qlgks1/Django-Redis-caching-scheduling-task-messaging-celery-async-worker)
- [how-to-use-redis-for-caching-and-pub-sub-in-python](https://betterprogramming.pub/how-to-use-redis-for-caching-and-pub-sub-in-python-3851174f9fb0)
- [redis publish / subscribe python example](https://blog.naver.com/PostView.naver?blogId=pareko&logNo=222528721348&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)

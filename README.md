# django-mq-series

This repository covers mq and pus/sub learning projects for redis, rabbitmq, kafka, nats, etc.

# Considerations before starting

## Build up dev environment using docker (django, celery, mariaDB, redis).

### \* But we do not take into account the test using Docker in this project.

- [Docker로 Django, Celery, Maria DB, Redis 개발 환경 설정하기](https://blog.khtinsoft.xyz/posts/django-celery-mariadb-redis-docker/)

# Project

## django-celery-rabbitmq

### preparation before start

- [RabbitMQ 윈도우 설치](https://afsdzvcx123.tistory.com/entry/RabbitMQ-RabbitMQ-%EC%84%A4%EC%B9%98)
- rabbitmq-plugins enable rabbitmq_management 입력 후, "Plugin configuration unchanged" 에러 발생시
  - [Spring Websocket & STOMP - 실시간 채팅 기능](https://velog.io/@toyou4203/%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%B1%84%ED%8C%85-%EA%B8%B0%EB%8A%A5)
  - 상위 링크의 본문에 있는 방법으로 해결 가능
    - rabbitmq-plugins.bat list 입력

### class info

- reference : [Learn Django Celery with RabbitMQ](https://www.youtube.com/watch?v=fBfzE0yk97k&list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20)
- original github : [YT-Django-Celery-Series-Intro-Install-Run-Task](https://github.com/veryacademy/YT-Django-Celery-Series-Intro-Install-Run-Task)

### note
- rabbitMQ
  - how to access the rabbitMQ with browser : http://localhost:15672/
  - id : guest, password : guest
- celery
  - install : pip install celery
  - how to run the celery on window : python -m celery -A config worker -l info -P gevent
  - run with log and pid info : celery -A config worker -l INFO -P threads -c 10 --pi
dfile="%n.pid" --logfile="%n.log"
- flower
  - install : pip install flower
  - how to access the rabbitMQ with browser : http://localhost:5555/
  - how to run the flower : celery -A config flower --port=5555
- celery-beat
  - install : pip install django-celery-beat
  - how to run the celery-beat : celery -A config beat -l INFO
  - how to run the celery-beat with database scheduler : celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    - remove CELERY_BEAT_SCHEDULE parameter at settings.py
- celery-result
  - install : pip install django-celery-results
  - update settins.py
    - add "django_celery_results" in INSTALLED_APPS =[]
    - add CELERY_RESULT_BACKEND = "django-db"
  - run migrate
  - monitoring method : admin page

## django-celery-redis-for-tasks
### class info
- reference : 
  - [무작정 시작하기 (1) - 설치 및 실행](https://heodolf.tistory.com/54)
  - [무작정 시작하기 (2) - Task](https://heodolf.tistory.com/63)
  - [무작정 시작하기 (3) - Chain](https://heodolf.tistory.com/65)
  - [무장적 시장하기 (4) - Group과 Chord](https://heodolf.tistory.com/66)
  - [무작정 시작하기 (5) - Monitoring](https://heodolf.tistory.com/73)
  - [How to Create a Celery Task Progress Bar in Django](https://www.youtube.com/watch?v=BbPswIqn2VI)
    - github : [djangoprogressbar](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/06/24/How%20to%20Create%20a%20Celery%20Task%20Progress%20Bar%20in%20Django)

### note
- celery
  - install : pip install celery
  - how to run the celery on window : python -m celery -A config worker -l info -P gevent
  - run with log and pid info : celery -A config worker -l INFO -P threads -c 10 --pi
dfile="%n.pid" --logfile="%n.log"
- flower
  - install : pip install flower
  - how to access the rabbitMQ with browser : http://localhost:5555/
  - how to run the flower : celery -A config flower --port=5555
- celery-beat
  - install : pip install django-celery-beat
  - how to run the celery-beat : celery -A config beat -l INFO
  - how to run the celery-beat with database scheduler : celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    - remove CELERY_BEAT_SCHEDULE parameter at settings.py
- celery-result
  - install : pip install django-celery-results
  - update settins.py
    - add "django_celery_results" in INSTALLED_APPS =[]
    - add CELERY_RESULT_BACKEND = "django-db"
  - run migrate
  - monitoring method : admin page
- celery-progress
  - install : pip install celery-progress
  - update settins.py
  - add ""celery_progress" in INSTALLED_APPS =[]

# reference :
## celery
- [celerry User Guid](https://docs.celeryq.dev/en/latest/userguide/index.html#guide)

## celery progress
- [How to Create a Celery Task Progress Bar in Django](https://www.youtube.com/watch?v=BbPswIqn2VI)
    - github : [djangoprogressbar](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/06/24/How%20to%20Create%20a%20Celery%20Task%20Progress%20Bar%20in%20Django)
- [Celery Progress Bars for Django](https://github.com/czue/celery-progress)
- [Managing asynchronous backend tasks with Django and Celery](https://procogia.com/managing-asynchronous-backend-tasks-with-django-and-celery/)

## rabbitMQ
- [official rabbitMQ tutorial site](https://www.rabbitmq.com/getstarted.html)
- [무작정 시작하기 (1) - 설치 및 실행](https://heodolf.tistory.com/50)
- [무작정 시작하기 (2) - Publish/Subscribe](https://heodolf.tistory.com/51)
- [무작정 시작하기 (3) - 환경설정](https://heodolf.tistory.com/53)

## redis queue
- [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
- [Django에 Celery 적용하기 첫번째 - 1 ](https://lucky516.tistory.com/2)
- [Django에서 Celery 이용하기 두번째 - 2 ](https://lucky516.tistory.com/3)
- [Celery beat으로 주기적으로 tasks 수행하기 - 3 ](https://lucky516.tistory.com/18)
- [Django - Celery 구성하기 - 1 ](https://asecurity.dev/entry/Django-Celery-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
- [Django - Celery로 비동기 Async Task 구성하기 - 2 ](https://asecurity.dev/entry/Django-Celery%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-Async-Task-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
- [장고(Django)에서 셀러리(Celery) 사용하기 1편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-1/)
- [장고(Django)에서 셀러리(Celery) 사용하기 2편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-2/)
- [장고(Django)에서 셀러리(Celery) 사용하기 3편](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-3/)
- [(Python) Django에서 Celery 사용하기(Broker-redis, docker-compose)](https://velog.io/@anjaekk/Python-Celery)
- [Celery + Redis](https://velog.io/@nameunzz/Celery-Redis)
- [First steps with Django (official site)](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django)
- [Send Async Emails In Your Django App With Celery And Redis \*\*\*](https://python.plainenglish.io/send-async-emails-in-your-django-app-with-celery-and-redis-137e0c454a0c)
- [Celery + Redis + Django \*\*\*](https://www.codingforentrepreneurs.com/blog/celery-redis-django/)
- [(Celery) 무작정 시작하기 시리즈 with python](https://heodolf.tistory.com/73)
- [분산 비동기 작업 처리를 위한 Celery 첫걸음](https://jonnung.dev/python/2018/12/22/celery-distributed-task-queue/#gsc.tab=0)
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

## monitoring

- [Monitoring and Management Guide](https://docs.celeryq.dev/en/latest/userguide/monitoring.html#guide-monitoring)
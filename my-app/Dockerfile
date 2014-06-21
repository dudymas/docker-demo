
FROM dockerfiles/django-uwsgi-nginx

RUN apt-get install inetutils-ping
RUN pip install pymongo

EXPOSE 80

WORKDIR /home/docker

CMD python app/myproj/manage.py runserver 0.0.0.0:80
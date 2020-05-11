FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD store/ /code/
ADD scripts/ /code/

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client
ENTRYPOINT ["./entrypoint.sh"]

CMD ./run.sh



FROM python:3.11.1
COPY . /everest_task
WORKDIR /everest_task
COPY ./docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
RUN chmod +x /everest_task/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
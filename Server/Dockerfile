FROM python:3.10

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

# CMD ["pytho3", "manage.py", "runserver", "0.0.0.0:8000"]

# uwsgi server
# FROM python:3.8.2
# LABEL maintainer twtrubiks
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /docker_api
# WORKDIR /docker_api
# COPY . /docker_api
# RUN pip install -r requirements.txt
# # RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt

# # for entry point
# RUN chmod +x /docker_api/docker-entrypoint.sh
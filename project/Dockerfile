

FROM python:3.10.1-slim-buster

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


#add app
COPY . .

#adding entrypoint.sh

# COPY ./entrypoint.sh .
# RUN chmod +x /usr/src/app/entrypoint.sh

# Run rntrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

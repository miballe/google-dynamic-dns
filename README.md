# google-dynamic-dns
Python client to update a Google Domains Dynamic record

## Build Image
In the local folder run:

```
docker build -t google-dyndns .
```
This will create a new container image called `google-dyndns`. Remind to use `sudo` in case your deployment requires higher priviledges.

## Start Container Instance
The best option to start the container image is using `docker-compose`. This is file template.

```
version: "3.7"

services:
  google-dyndns:
    image: google-dyndns
    container_name: googledns
    environment:
      - GOOGLE_DNS_USER=Vs9ERF99hbfp8H7S,RshDIc9WWwwb3fR9
      - GOOGLE_DNS_PWD=z5BfD885TaAKrrAL,EQ44FfqLsLNwKeNA
      - GOOGLE_DNS_RECORD=domain1.com,domain2.com
      - DETECT_IP=True
      - NEW_IP=0.0.0.0
      - UPDATE_INTEVAL_MINS=5
      - PYTHONUNBUFFERED=1
    restart: always
```

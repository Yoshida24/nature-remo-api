FROM --platform=linux/x86_64 python:3.10.6-slim-buster

ARG nature_access_token 
ARG nature_appearance
ARG line_notify_token

ENV NATURE_ACCESS_TOKEN=$nature_access_token \
    NATURE_APPEARANCE=$nature_appearance \
    LINE_NOTIFY_TOKEN=$line_notify_token

RUN mkdir -p /app/
COPY app/src /app/

RUN pip install --upgrade pip==22.2.2
RUN pip install requests==2.28.1 

ENTRYPOINT ["python", "/app/main.py"]
CMD []
FROM python:3.11.1-alpine3.17

WORKDIR /usr/src/app

RUN apk update && apk add curl git bash
COPY requirements.txt /usr/src/app
COPY app.py /usr/src/app
COPY tblArray.json /usr/src/app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080"]

#CMD [ "gunicorn", \
#      "-b", "0.0.0.0:8080", \
#      "--env", "SCRIPT_NAME=/", \
#      "-w", "8", \
#      "--timeout", "300", \
#      "--keep-alive", "30", \
#      "--threads", "24",\
#      "--preload", \
#      "app:app" ]

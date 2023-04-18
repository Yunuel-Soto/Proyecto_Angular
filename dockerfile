FROM python:3.10-slim

WORKDIR /PROYECTO
COPY Logica ./Logica
COPY Api-Rest ./Api-Rest 
COPY requeriments.txt .
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt
ENV PYTHONPATH="$PYTHONPATH:/"

EXPOSE 8000
CMD ["python", "./Api-Rest/Proyecto/manage.py", "runserver", "0.0.0.0:8000"]
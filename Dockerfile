# python:alpine is 3.{latest}
FROM python:alpine

COPY script /script 

RUN pip3 install -r /script/module.txt
RUN python3 /script/csvToDb.py 

COPY Flask-Restful /src/

EXPOSE 8000

ENTRYPOINT ["python3", "/src/api.py"]
FROM python:3.9.7

RUN echo "testing123"

WORKDIR /home/

RUN git clone https://github.com/TKJung/Account-API.git

WORKDIR /home/Account-API/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 3030

CMD ["python", "manage.py", "runserver", "127.0.0.1:3030"]
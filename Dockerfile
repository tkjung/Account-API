FROM python:3.8.8

RUN echo "testing123"

WORKDIR /home/

RUN git clone https://github.com/lee-JunR/accounteapi.git

WORKDIR /home/accounteapi/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 5050

CMD ["python", "manage.py", "runserver", "0.0.0.0:5050"]
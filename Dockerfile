FROM python:3.8

RUN apt-get update
#copy application code
WORKDIR /var/app
COPY . .
COPY requirements.txt .

#fetch app specific dependencies

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#Expose port

EXPOSE 5000

#start app

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

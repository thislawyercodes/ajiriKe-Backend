FROM python:3.8
RUN pip install --upgrade pip  
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . code
WORKDIR /code
EXPOSE  8000
CMD python manage.py runserver  


# ajiriKe-Backend

The  backend  application for ajiriKe -a fresh-graduates/ entry level job seeking platform.

# How to setup the project locally


Clone the repository as you usually would.
----------------------

Set up your virtual environment
----------------------
``` shell
python3 -m venv env
```
Activate your virtual environment
----------------------
``` shell
source env/bin/activate
```
Install the required packages
----------------------
``` shell
python3 -m pip install -r requirements.txt 
```
Create a .env file with the following environment variables
------------------------------------------------------------------
``` shell
SECRET_KEY=yoursecretkey
DATABASE_NAME=yourdb
DATABASE_USER=yourdbuser
DATABASE_PASSWORD=yourbdpassword
DATABASE_HOST=localhost
DATABASE_PORT=''
```
Export your environment variables
--------------------------------------------
``` shell
source .env
```
Create a local database with the credentials in your .env file
---------------------------------------------------------------

Run migrations
----------------------
``` shell
python3 manage.py makemigrations
```
Migrate database updates
----------------------
``` shell
python3 manage.py migrate
```
Run Unit Tests
----------------------
``` 
```
Start local server
----------------------
``` shell
python3 manage.py runserver
```
Swagger Technical Documentation
----------------------
``` shell
http://127.0.0.1:8000/swagger/


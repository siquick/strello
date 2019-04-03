# Strello API

## Available at `strello.ekhry3m6if.ap-southeast-2.elasticbeanstalk.com`  


Written in Django & DRF with MySQL database  
Hosted at AWS (Elastic Beanstalk)  
Schema in Swagger  



### Requirements
`python3` `pip` `virtualenv`


### How to run on local:

`$ git clone https://github.com/siquick/strello`  
`$ cd strello`  
`$ virtualenv -p python3 venv`     
`$ nano venv/bin/activate`  
past environment variables to the bottom of this file (see below)  
`$ source venv/bin/activate`  
`$ pip install -r requirements.txt`  
`$ python manage.py makemigrations`  
`$ python manage.py migrate`  
`$ python manage.py runserver`


### Endpoints
Prepend with `http://127.0.0.1:8000` for local or `http://strello.ekhry3m6if.ap-southeast-2.elasticbeanstalk.com` for production.

`/members/` accepts  `GET, POST, HEAD, OPTIONS`  
`/member/<member_id>`  
`/boards/` accepts  `GET, POST, HEAD, OPTIONS`
`/board/<board_id>`  accepts `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`  
`/lists/` accepts  `GET, POST, HEAD, OPTIONS`  
`/list/<list_id>`  accepts `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`   
`/cards/` accepts  `GET, POST, HEAD, OPTIONS`  
`/card/<card_id>`  accepts `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`   
`/labels/` accepts  `GET, POST, HEAD, OPTIONS`  
`/label/<label_id>`  accepts `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`     

`POST` = create  
`PUT` = edit (includes archive)  
`GET` = retrieve  


#### Tests

`python manage.py test`


#### Environment Variables
You will need to set the following environment variables (these go in `venv/bin/activate`)

`export SECRET_KEY='your-secret-key'`  
`export DEBUG=<BOOLEAN>`  
`export DB_ENGINE='your-db-backend'`  
`export DB_NAME='your-db-name'`  
`export DB_USER='your-db-username'`  
`export DB_PASSWORD='your-db-pwd'`  
`export DB_HOST='your-db-host'`  
`export DB_PORT='your-db-port'`  
`export INTERNAL_IPS=['your-internal-ip']`  
`export ALLOWED_HOSTS=['you-allowed-hosts']`  

Example variables using SQLite3 on local environment

`export SECRET_KEY='asldk;alskd;alskd;laskd;laskd;la'`  
`export DEBUG=True`  
`export DB_ENGINE='django.db.backends.sqlite3'`  
`export DB_NAME=os.path.join(BASE_DIR, 'db.sqlite3')`  
`export DB_USER=''`  
`export DB_PASSWORD=''`  
`export DB_HOST=''`  
`export DB_PORT=''`  
`export INTERNAL_IPS=['127.0.0.1','localhost']`  
`export ALLOWED_HOSTS=['*']` 


#### Enhancements in next iteration

Authentication / Authorization

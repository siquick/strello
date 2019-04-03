# Strello API

Written in Django & DRF with MySQL database  
Hosted at AWS Elastic Beanstalk
Schema in Swagger  
Available at `strello.ekhry3m6if.ap-southeast-2.elasticbeanstalk.com`

### Requirements
`python3` `pip` `virtualenv`

### How to run on local:

`$ git clone https://github.com/siquick/strello`  
`$ cd strello`  
`$ virtualenv -p python3 venv`     
`$ nano venv/bin/activate`  
past environment variables to the bottom of this file (see below)  
`$ pip install -r requirements.txt`  
`$ python manage.py makemigrations`  
`$ python manage.py migrate`  
`$ python manage.py runserver`

#### Tests

`python manage.py test`

#### Environment Variables
You will need to set the following environment variables (these can usually go in <virtualenvname>/bin/activate)

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
`export INTERNAL_IPS=['127.0.0.1','localhost]`  
`export ALLOWED_HOSTS=['*']` 




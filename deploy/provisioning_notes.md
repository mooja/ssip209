## Install Required System Packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

 - package names: nginx git python3 python3-pip pip3 install virtualenv


## Create Folder Structure for the django app:
/srv
└── webapps
    └── sitename
         ├── database
         ├── source
         ├── static
         └── virtualenv


* git pull the app and save it as sitename

## Create a Virtual Environemtn for the django app

cd sitedir && pip install -r requirements/production


## create Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## create Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com
* upload envdirs


## Migrate database schema & data
cd into site_root && exec "./manage.py mikemigrations"

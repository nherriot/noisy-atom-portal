# Noisy Atom Portal

This text document explains the setup of the Noisy-Atom portal. The Noisy Atom portal is a Django based web server serving up the NoisyAtom home page, blog and example project work.

Ubuntu 18.04 is the targeted platform. This should run on Ubuntu 20.xx as is but not tested thoroughly.

## Setup Python 3.8
The portal is based on Python version 3.8. This may not be supported on your current version of Linux. 
To get access to all the features we need 3.8 on your local machine. For this I used the [Deadsnake PPA](https://github.com/deadsnakes) which holds a number of pre-compiled python versions for Ubuntu.

You can follow this link and instructions, however to reduce context switching you can follow commands here:

```
/> sudo apt update
/> sudo add-apt-repository ppa:deadsnakes/ppa
/> sudo apt update
/> sudo apt install python3.8
```

## Installing Non-default Linux Packages
The portal uses **postgres** as it's backend database. For this the python package psycopg2 will be installed.
However, this requires the installation of several Linux packages which may not be on your default system. You
need to have libpq-dev, python-dev, and python3.8-dev python development libraries since there will be compiled python
binaries dependent on header files being available. To do this:

```bash
    /> sudo apt-get install libpq-dev python-dev python3.8-dev
```

The **Pillow** python graphics package also requires the following **zlib** and **jpeg** libraries which also may not
be part of your vanilla setup. Install the Linux zlib packages. To do this:

```bash

  /> sudo apt install libjpeg8-dev zlib1g-dev

```

## Install virtualenv & virtualenvwrapper
Detailed instructions are [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

```bash
/> sudo pip install virtualenvwrapper
    Collecting appdirs==1.4.0
      Using cached appdirs-1.4.0-py2.py3-none-any.whl (11 kB)
    Collecting Django==1.10.5
      Using cached Django-1.10.5-py2.py3-none-any.whl (6.8 MB)
    Collecting django-bootstrap4==0.0.4
      Using cached django_bootstrap4-0.0.4-py3-none-any.whl
    Collecting django-markdown-deux==1.0.5
      Using cached django_markdown_deux-1.0.5-py3-none-any.whl
    Collecting django-pagedown==0.1.3
      Using cached django_pagedown-0.1.3-py3-none-any.whl
    Collecting django-crispy-forms==1.6.1
      Using cached django_crispy_forms-1.6.1-py2.py3-none-any.whl (103 kB)
    Collecting gunicorn==19.6.0
      Using cached gunicorn-19.6.0-py2.py3-none-any.whl (114 kB)
    Collecting Markdown==2.6.9
      Using cached Markdown-2.6.9-py3-none-any.whl
    Collecting markdown2==2.3.4
      Using cached markdown2-2.3.4-py3-none-any.whl
    Collecting olefile==0.44
      Using cached olefile-0.44-py3-none-any.whl
    Collecting packaging==16.8
      Using cached packaging-16.8-py2.py3-none-any.whl (23 kB)
    Collecting Pillow==4.0.0
      Using cached Pillow-4.0.0-cp38-cp38-linux_x86_64.whl
    Collecting psycopg2==2.8
      Using cached psycopg2-2.8-cp38-cp38-linux_x86_64.whl
    Collecting pyparsing==2.2.0
      Using cached pyparsing-2.2.0-py2.py3-none-any.whl (56 kB)
    Collecting six==1.11.0
      Using cached six-1.11.0-py2.py3-none-any.whl (10 kB)
    Installing collected packages: six, pyparsing, olefile, markdown2, Django, psycopg2, Pillow, packaging, Markdown, gunicorn, django-pagedown, django-markdown-deux, django-crispy-forms, django-bootstrap4, appdirs
    Successfully installed Django-1.10.5 Markdown-2.6.9 Pillow-4.0.0 appdirs-1.4.0 django-bootstrap4-0.0.4 django-crispy-forms-1.6.1 django-markdown-deux-1.0.5 django-pagedown-0.1.3 gunicorn-19.6.0 markdown2-2.3.4 olefile-0.44 packaging-16.8 psycopg2-2.8 pyparsing-2.2.0 six-1.11.0
    WARNING: You are using pip version 21.1.2; however, version 22.0.3 is available.
    You should consider upgrading via the '/home/<your-dir>/virtualenv/noisy-atom/bin/python -m pip install --upgrade pip' command.
    />



```

## Setup a Virtual Environment
In this case we are using the project name 'noisy-atom'
Hence from your home directory do:

```bash
/> mkvirtualenv --python=/usr/bin/python3.8 noisy-atom
/> workon noisy-atom
(noisy-atom)nherriot@kieran ~/virtualenv/noisy-atom
```
To verify the correct version is installed you can type:

```
/>
/> python --version
   Python 3.8.12
```

## Clone your Repository
Using git clone the repo
```bash
/> git clone https://github.com/nherriot/noisy-atom-portal.git
```

## Check Python Path and Install Required Django packages
If you have virtual environments you may have your python path setup in the postactivate
script within your virtualenvironment. Check within ~/virtualenv/postactivate. 
e.g.

```bash
/> cd ~/virtualenv/<project name>/bin
/> nano postactivate
```
Add the line:
```bash
export DJANGO_SETTINGS_MODULE=noisy-atom.settings_nherriot
```
Install requirements for the python django project
```bash
/> cd ~/virtalenv/noisy-atom/noisy-atom-portal/noisyatom
/> pip install -r requirements.txt
```

## Check The Django Application Works

### Use The Runserver To Check It Works
Within the python directory use the **runserver** development tool to check it works:
```bash
/> cd ~/home/nherriot/virtalenv/noisy-atom/noisy-atom-portal/noisyatom
/> python manage.py runserver
System check identified no issues (0 silenced).
March 22, 2016 - 22:27:14
Django version 1.9.2, using settings 'wine_apps.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Not Found: /favicon.ico
[22/Mar/2016 22:27:21] "GET /favicon.ico HTTP/1.1" 404 6893
```

### Check On Local Browser
Check this work on your local browser by going to the URL:
```bash
localhost:8000
```

## Change Database To Postgres
If you don't have 'postgres' installed on your machine you can install with the following packages:
```bash
/> sudo apt-get install postgresql-contrib
/> sudo apt-get install postgresql-server-dev-9.3
/> sudo apt-get install postgresql-client
/> sudo apt-get install pgadmin3
```

Make sure you have the python library that lets you interface to 'Postgres'. For more information on
this you can [read](https://docs.djangoproject.com/en/1.9/ref/settings/#databases).
First install the package with:
```bash
/> sudo apt-get install python-psycopg2
```
Update your postgres database to contain a user called ffw_user, and a database called 'ffw'. This will require you to switch to the **postgres** user on your terminal window, get on to the posgres admin interface and add the DB and user.
```bash
/> sudo -i -u postgres				# login as postgres super user
/> psql						# use the postgres cli interface
	psql (9.3.10)
	Type "help" for help.
/> postgres=#  CREATE DATABASE na_db;		# Create a database on the psql command prompt
CREATE DATABASE

/> postgres=# CREATE USER na_db_user WITH PASSWORD 'na_user';		# create the user and passwprd
CREATE ROLE

/> postgres=# GRANT ALL PRIVILEGES ON DATABASE na_db to na_db_user;		# grant privillages to the user
GRANT
postgres=#

/> postgres=# \l				# View your databases to make sure it is on your system

                                    List of databases
     Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
---------------+----------+----------+-------------+-------------+-----------------------
 alfa          | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =Tc/postgres         +
               |          |          |             |             | postgres=CTc/postgres+
               |          |          |             |             | alfa=CTc/postgres
 alfa_26102015 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =Tc/postgres         +
               |          |          |             |             | postgres=CTc/postgres+
               |          |          |             |             | alfa=CTc/postgres
 alfa_30092015 | alfa     | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 |
 ffw           | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =Tc/postgres         +
               |          |          |             |             | postgres=CTc/postgres+
               |          |          |             |             | ffw_user=CTc/postgres
 postgres      | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 |
 template0     | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
(7 rows)

```

Note for development you may want to rebuild database and run test cases. This will require your user the ability to create, destroy databases. As well as become owner of the database they work on. There are 2 commands for this.
1. To allow a user to create and destory databases - which will be needed if that user wants to create test databases during testing you can use:

postgres=# ALTER USER na_db_user CREATEDB;

2. To have your user 'own' a database allowing them to reset and drop all tables which you may want to do for resetting migrattions you can use:
```bash
postgres=# ALTER USER na_db_user CREATEDB;ALTER DATABASE na_db OWNER TO na_db_user;
/> postgres=# \q					# Quit the psql interface and exit as this user
$ exit
```
Update your settings file to talk to your postgres DB. This should be unique to your local database. In this instance, you need to make it unique to the database on your local machine for your DEV environment and not your production environment.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'na_db',
        'USER': 'na_db_user',
        'PASSWORD': 'na_user',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'na_db_17022016',					# This is our database name
        'USER': 'na_db_user',						# This is the user of our database
        'PASSWORD': 'xxxxx',						# This is the password of the database user
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Install the python postgres SQL adapter
```bash
(ffwines)/> pip install psycopg2
```

Make sure you update the requiremetns.txt file if it's not changed already. You can check out that you have access to the database like this:
```bash
(noisy-atom)/> python manage.py shell
***** WARNING! This is a non-production build *****
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>from django.db import connection
>>> from django.db import connection
>>> cursor = connection.cursor()
>>> quit()
```

If nothing happens then your server is working properly with the database. Next we need to migrate the new database and check the migration worked.

```bash
(noisy-atom)/> python manage.py migrate			# Migrate the database.
(noisy-atom)/> python manage.py showmigrations		# Check it worked.

accounts
 [X] 0001_initial
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
cms
 [X] 0001_initial
 [X] 0002_news_user
 [X] 0003_news_draft
 [X] 0004_auto_20160306_1254
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
profiles
 [X] 0001_initial
registration
 [X] 0001_initial
 [X] 0002_registrationprofile_activated
 [X] 0003_migrate_activatedstatus
sessions
 [X] 0001_initial
sites
 [X] 0001_initial
 [X] 0002_alter_domain_unique
```

## Check Your Server Works
Update your virtual env python file to contain the postgres adapter
```bash
(noisy-atom)/> python manage.py createsuperuser
(noisy-atom)/> python manage.py runserver
```







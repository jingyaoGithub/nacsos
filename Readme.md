# NACSOS: NLP Assisted Classification, Synthesis and Online Screening Setup on Windows

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4121525.svg)](https://doi.org/10.5281/zenodo.4121525)

Authors: Max Callaghan, Jérôme Hilaire, Finn Müller-Hansen, Yuan Ting Lee

## Summary

NACSOS is a django site for managing collections of documents, screening or coding them by hand, and doing NLP tasks with them like topic modelling or classifiation.

It was built for handling collections of scientific document metadata, but has extensions that deal with twitter data and parliamentary data.

It currently contains many experimental, redundant or unsupported features, and is not fully documented.

The part that deals with topic modelling is a fork of Allison J.B Chaney's **tmv** [repository](https://github.com/blei-lab/tmv). It extends this by managing multiple topic models and linking these with various document collections.

NACSOS is research software produced by the APSIS working group at the Mercator Research Institute on Global Commons and Climate Change ([MCC](https://www.mcc-berlin.net/)), and some parts of the repository are instution specific. We are in an ongoing process of generalising, and documenting.

Refer to the [documentation](https://github.com/mcallaghan/tmv/wiki/Scoping-Documentation) for a (partial) guide to using the app.

## Citation

If you use NACSOS in academic work, you can cite it as

Max Callaghan, Finn Müller-Hansen, Jérôme Hilaire, & Yuan Ting Lee. (2020). NACSOS: NLP Assisted Classification, Synthesis and Online Screening. Zenodo. http://doi.org/10.5281/zenodo.4121525


## A general guide to installation

The following instructions assume installation on Windows with Python 3.7

### Setting up PostgreSQL

If you do not have PostgreSQL installed already, install it. At time of writing, the latest release was PostgreSQL 14. This version is assumed. We also need postgis to handle geographical data

Download and install from https://www.postgresql.org/download/

Start a Command Prompt and type
```
psql -U postgres
```
***IF ERROR PSQL Failure 5432:**
Control panel - Administrative tools - Services - postgresql X64 (right click and start)*


Create a new user for this app (call it whatever you like), use a secure password, in single quotes:
```
CREATE USER scoper WITH PASSWORD 'YOUR_PASSWORD';
```

Create a database for the app, use whatever name you like:
```
CREATE DATABASE scoping_tmv OWNER scoper;
```

Connect to the database and create a postgis extension

```
\connect scoping_tmv;
CREATE EXTENSION postgis;
```

Create a trigram extension

```
CREATE EXTENSION pg_trgm;
```

Quit PostgreSQL and log out of the postgres user role

```
\q
exit
```

### Setting up Celery (Not necessary could skip at first)
We use celery to execute computation-heavy tasks in the background.

To do this we need to install the *message broker* RabbitMQ, install ERLANG before installing RabbitMQ on Winodws, instruction could be found on the offical page of RabbitMQ 

After installation open RabbitMQ run 
```
celery -A celery worker --loglevel=INFO --pidfile='’
```


### Setting up scoping-tmv

Operating in a virtual environment is **highly** recommended

Recommended Python version is 3.7

Check this video if you are interested in operating multiple Python versions on Windows: https://www.youtube.com/watch?v=HTx18uyyHw8&list=LL&index=4&t=613s

Set directory to the BasicBrowser folder
```
cd X:\...\nacsos\BasicBrowser

pip install virtualenv

python -m venv .venv
.venv\Scripts\activate

```


Once in the environment, install dependencies, use requirements_min.txt, 5 packages might need to install separately 

```
pip install -r requirements_min.txt
pip install multiprocess==0.70.8
pip install psycopg2==2.8
pip install markdown
pip install lda
pip install gensim==3.2.0
pip install pandas==0.23.4
```

This can take a while...

### GDAL installation 
GDAL 2.2.4 is recommanded for Python 3.7 and Django 2.2.2, run the following 
```
python -m pip install GDAL-2.2.4-cp37-cp37m-win_amd64.whl
```

### The real start
Now you need to modify the setting_local.py file in the directory ...\nacsos\BasicBrowser\BasicBrowser, change the Password to what you set before

Check and trial 

```
python manage.py check
```

Migrate
```
python manage.py migrate
```

Create an admin user if using on a clean database

```
python manage.py createsuperuser
```

Now you should be done, and ready to run a local server

```
python manage.py runserver
```

If everything set correctly, you would see:
```
System check identified no issues (0 silenced). 
```


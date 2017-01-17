# CS-C3170 Web Software Development Project Plan

# 0. Setup
Install python 3.5:
https://www.python.org/downloads/release/python-352/

Install the Heroku CLI:
https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Install Postgres:
https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

If Postgres complains about user on server start:
 in settings.py / DATABASES / "default", change NAME and USER to your local username. Don't commit this file!

# 1.Running the test in local environment
    `virtualenv venv` //create a virtualenv for the app;
    `source venv/bin/activate`//activate the virtualenv;
    `pip install -r requirements.txt` //install the dependencies
    `python manage.py collectstatic`  //respond with yes.
    `heroku local` //run the web locally

 If you get a "Command "python setup.py egg_info" failed with error code 1...", on os x try:
 sudo pip3 install git+https://github.com/donnemartin/gitsome.git
 
 
 #### If you don't want to run in Heroku, try instead: ####
     `virtualenv venv`
     `source venv/bin/activate`
     `pip install -r requirements.txt` //only need to run this once
     `python manage.py makemigrations` 
     `python manage.py migrate`
     `python manage.py runserver`

Then test in your browser at e.g. http://localhost:8000/index/
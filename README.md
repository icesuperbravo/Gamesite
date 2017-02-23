# CS-C3170 Web Software Development Project Plan

# The project is uploaded to the could platform Heroku, and you can have access to http://wsd2016.heroku.com
# 0. Setup
Install python 3.5:
ref: https://www.python.org/downloads/release/python-352/

Install the Heroku CLI:
ref: https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Install Postgres:
ref: https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

Install Crispyforms:
pip install --upgrade django-crispy-forms

If Postgres complains about user on server start:
 in settings.py / DATABASES / "default", change NAME and USER to your local username. Don't commit this file!

Install crispy form:

ref: http://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms  
 
The Gamesite uses **Bootstrap** framework for the frontend design. details on:

ref: http://getbootstrap.com/

Install social-auth-app-django for 3rd party login:

`pip install social-auth-app-django`

ref: https://pypi.python.org/pypi/social-auth-app-django/

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

To kill the server (OS X):

    `pkill -f 'python manage.py runserver'`
or  
    
    `pkill -f python`
    
# 2. Running the local email server to test registration emailing function:

Python has a little SMTP server built-in. You can start it in a second console with this command:

`python -m smtpd -n -c DebuggingServer localhost:1025`

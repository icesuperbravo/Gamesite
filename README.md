# CS-C3170 Web Software Development Project Plan

# 0. Setup
Install python 3.5:
https://www.python.org/downloads/release/python-352/

Install the Heroku CLI:
https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Install Postgres:
https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

# 1.Running the test in local environment
 `virtualenv venv` //create a virtualenv for the app;
 `source venv/bin/activate`//activate the virtualenv;
 `pip install -r requirements.txt` //install the dependencies
 `python manage.py collectstatic`  //respond with yes.
 `heroku local` //run the web locally

 If you get a "Command "python setup.py egg_info" failed with error code 1...", on os x try:
 sudo pip3 install git+https://github.com/donnemartin/gitsome.git
 
 

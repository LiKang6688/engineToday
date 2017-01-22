# engineToday

1. Make sure you have Python 2.7.6, virtualenv, pip and sqlite3 installed


2. Go to project home folder and run these commands to create a virtual environment and activate it:

    virtualenv enginetoday
    cd enginetoday
    source bin/activate

3.  Use pip to install dependencies with:

    pip install -r requirements.txt

4. Now we have to prepare a database:

    python manage.py migrate

    or

    python manage.py syncdb

    python manage.py makemigrations

    and we can check if it able to run

    python manage.py check

5. Run django server

    python manage.py runserver

    and go to http://127.0.0.1:8000

6. create root

    python manage.py createsuperuser
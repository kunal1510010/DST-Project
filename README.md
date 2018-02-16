# DST-Project
Prerequisites: Python and pip

step 1: install virtualenv
run command
# sudo pip3 install virtualenv 

step 2: create a virtualenv named 'venv' in the root diretory
# virtualenv venv

step 3: start virtualenv
# source /env/bin/activate

step 4: install django in virtualenv
# pip install django

step 5: run migrate command (for migrations)
# python manage.py migrate

step 6: run python-django server
# python manage.py runserver

Notes: client-angular folder contains the dist folder which holds the static angular files.
These need to be transferred to django app (the js files to *Project*/static and index, favicon to "app"/templates.
Also index.html needs to be converted to static using %load static and js imports, to import files via % static

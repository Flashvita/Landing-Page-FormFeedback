#Install virtual environment

python3 -m install venv venv


#Activate

source venv/bin/activate

#Install requirements

pip install django==4.04

pip install crispy-bootstrap5

pip install Pillow==9.1.0


#Make migrate

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser


#Run project

python manage.py runserver

# Landing-Page-FormFeedbackython 
python3 -m install venv venv
source venv/bin/activate
pip install django==4.04
pip install crispy-bootstrap5
pip install Pillow==9.1.0
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

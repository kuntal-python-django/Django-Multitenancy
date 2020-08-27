# Multitenancy Application Using Django 2.2

python manage.py makemigrations

python manage.py migrate_schemas

python manage.py startapp Users

python manage.py startapp Books

python manage.py makemigrations

python manage.py migrate_schemas


To create tenant run bellow command

>> python manage.py shell < create_tenant.py


GET: http://tenant1.my-domain.com:8000/users/

POST: http://tenant1.my-domain.com:8000/users/

dataset:
{
    "name": "Kuntal Samanta",
    "username": "user1"
}
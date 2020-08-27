# Multitenancy Application Using Django 2.2

**Note
Isolated Approach: Separate Databases. Each tenant has it’s own database.
Semi Isolated Approach: Shared Database, Separate Schemas. One database for all tenants, but one schema per tenant.
Shared Approach: Shared Database, Shared Schema. All tenants share the same database and schema. There is a main tenant-table, where all other tables have a foreign key pointing to.

Here we are following Semi Isolated Approach


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

from Accounts.models import Client

""" 
    don't add your port or www here! on a local server you'll want to use localhost here
    don't add your port or www here
"""
# create your public tenant
tenant = Client(
    domain_url='my-domain.com',
    schema_name='public',
    name='public_tenant'
    )
tenant.save()

# create your first real tenant
tenant1 = Client(
    domain_url='tenant1.my-domain.com',
    schema_name='tenant1',
    name='private_tenant1'
    )
# migrate_schemas automatically called, your tenant is ready to be used!
tenant1.save()

tenant2 = Client(
    domain_url='tenant2.my-domain.com',
    schema_name='tenant2',
    name='private_tenant2'
    )
# migrate_schemas automatically called, your tenant is ready to be used!
tenant2.save()

tenant3 = Client(
    domain_url='tenant3.my-domain.com',
    schema_name='tenant3',
    name='private_tenant3'
    )
# migrate_schemas automatically called, your tenant is ready to be used!
tenant3.save()

tenant4 = Client(
    domain_url='tenant4.my-domain.com',
    schema_name='tenant4',
    name='private_tenant4'
    )
# migrate_schemas automatically called, your tenant is ready to be used!
tenant4.save()
# Generated by Django 2.1.7 on 2019-02-23 18:38

from django.db import migrations


def add_companies(apps, schema_editor):
    """
    Agregar compañia por default

    """
    company_model = apps.get_model('clients', 'Company')
    company_model.objects.create(
        name='Company One',
        contact_phone='9879879871',
        support_phone='9879879872',
        sales_phone='9879878973',
    )
    company_model.objects.create(
        name='Company Two',
        contact_phone='9879879871',
        support_phone='9879879872',
        sales_phone='9879878973',
    )
    company_model.objects.create(
        name='Company Three',
        contact_phone='9879879871',
        support_phone='9879879872',
        sales_phone='9879878973',
    )


def link_clients_to_companies(apps, schema_editor):
    company_model = apps.get_model('clients', 'Company')
    client_model = apps.get_model('clients', 'Client')

    default_company = company_model.objects.get(pk=1)

    for client in client_model.objects.all():
        if not client.company:
            client.company = default_company
            client.save()


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_add_client_company'),
    ]

    operations = [
        migrations.RunPython(add_companies),
        migrations.RunPython(link_clients_to_companies)
    ]

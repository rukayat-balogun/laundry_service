# Generated by Django 3.2.3 on 2021-05-26 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_services_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='name',
            new_name='item',
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_name_services_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
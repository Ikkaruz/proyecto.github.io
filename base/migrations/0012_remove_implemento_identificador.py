# Generated by Django 3.2.2 on 2021-05-14 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_implemento_identificador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='implemento',
            name='identificador',
        ),
    ]

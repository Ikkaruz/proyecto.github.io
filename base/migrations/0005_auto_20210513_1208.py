# Generated by Django 3.2.2 on 2021-05-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_prestamo_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implemento',
            name='cantidad_disponible',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='implemento',
            name='cantidad_prestada',
            field=models.IntegerField(),
        ),
    ]

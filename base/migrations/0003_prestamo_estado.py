# Generated by Django 3.2.2 on 2021-05-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210512_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='estado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

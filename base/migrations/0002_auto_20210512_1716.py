# Generated by Django 3.2.2 on 2021-05-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.RemoveField(
            model_name='implemento',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='implemento',
            name='nombre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
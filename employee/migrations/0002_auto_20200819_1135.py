# Generated by Django 3.0.6 on 2020-08-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmployeeStatus',
            field=models.BooleanField(default=True),
        ),
    ]
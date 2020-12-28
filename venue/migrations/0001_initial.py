# Generated by Django 3.0.5 on 2020-08-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('VenueId', models.AutoField(primary_key=True, serialize=False)),
                ('VenueName', models.CharField(max_length=150)),
                ('VenueImageName', models.TextField(blank=True, null=True)),
                ('VenueImage', models.ImageField(blank=True, null=True, upload_to='images')),
                ('VenueLocation', models.TextField()),
            ],
        ),
    ]
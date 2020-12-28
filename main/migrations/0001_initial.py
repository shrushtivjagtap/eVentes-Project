# Generated by Django 3.0.5 on 2020-08-05 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('NotificationId', models.AutoField(primary_key=True, serialize=False)),
                ('NotificationTitle', models.TextField()),
                ('NotificationDescription', models.TextField()),
                ('NotificationDateTime', models.DateTimeField(auto_now=True)),
                ('AchievementId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='achievement.Achievement')),
                ('StudentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
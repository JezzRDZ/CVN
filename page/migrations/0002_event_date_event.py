# Generated by Django 2.2.1 on 2019-06-01 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_event',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-01 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_track_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 18, 53, 24, 39640, tzinfo=datetime.timezone.utc), verbose_name='date uploaded'),
        ),
    ]

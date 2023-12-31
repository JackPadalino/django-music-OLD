# Generated by Django 4.2.8 on 2023-12-31 23:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_track_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 31, 23, 53, 46, 91797, tzinfo=datetime.timezone.utc), verbose_name='date uploaded'),
        ),
    ]

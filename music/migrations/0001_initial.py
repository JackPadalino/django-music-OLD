# Generated by Django 4.2.8 on 2023-12-31 18:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])])),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
    ]
